# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:00:11 2020

@author: gyetm
Modul for soving the stationer model with the simple transition rules 

"""

#import B_end_gurobi as solver
#import backend_PulP_st_TR
#import backend_PulP_st_mTR
import consol
import calculation
import numpy as np



class util:
    def empty_solution(Object):
            Object.Premiums = []
            Object.Transition_rules = []
            Object.OP = 0
            Object.TOP = 0
    
    
class Optimise_joint():
    def __init__(self, Parameters):
        """ constructor """
        
        self.Types = [each for each in Parameters["Exp_claims"]]
        
        
        if Parameters["rule_type"] == "S" and Parameters["periods"] == 0:
            self.build_unified_rules(Parameters)

        elif Parameters["rule_type"] == "M" and Parameters["periods"] == 0:
            self.build_nonunified_rules(Parameters)
        else:
            self.build_multiperiod_model(Parameters)
        
        
        
    def build_unified_rules(self, Parameters):
        import backend_PulP_st_TR
        self.backend = backend_PulP_st_TR
        self.base_backend = backend_PulP_st_TR
        self.J = [k for k in range(-Parameters["nbr_of_classes"]+1, Parameters["nbr_of_classes"])]   
    
    def build_nonunified_rules(self, Parameters):
        import backend_PulP_st_mTR
        self.backend = backend_PulP_st_mTR
        import backend_PulP_st_TR
        self.base_backend = backend_PulP_st_TR
        
        self.J = np.empty([Parameters["nbr_of_classes"], Parameters["nbr_of_classes"]], int)
        for k in range(Parameters["nbr_of_classes"]):
              for s in range(Parameters["nbr_of_classes"]):
                self.J[k][s] = -k+s
                
    def build_multiperiod_model(self, Parameters):
        import backend_PulP_mp_TR
        self.backend = backend_PulP_mp_TR
        self.J = [k for k in range(-Parameters["nbr_of_classes"]+1, Parameters["nbr_of_classes"])]
        import backend_PulP_st_TR
        self.base_backend = backend_PulP_st_TR
        
        
        
    
    
    def build_Epsilon(self, Parameters):    
        
        self.Epsilon = [Parameters["Exp_claims"][i]- min(Parameters["Exp_claims"].values()) for i in self.Types 
                   if Parameters["Exp_claims"][i]> min(Parameters["Exp_claims"].values())]
        self.Epsilon.sort() 
     
    def build_model(self, Parameters):
        """set up the basic model"""
        self.model = self.backend.Setup_Joint_Model(Parameters, self.Types, self.J, self.Epsilon)
    
    def build_observable_model(self, Parameters):
        """ set up a model, where the observable parameters are also known """
        import backend_PulP_st_TR_obs
        
        self.Epsilon = set()

        for rgroup in Parameters["Exp_claims"]:
                difference = round(Parameters["Exp_claims"][rgroup] - Parameters['Obs_claims'][rgroup],4)
                if difference != 0:
                    self.Epsilon.add(difference)
        
        self.Epsilon = list(self.Epsilon)
       
        self.model = backend_PulP_st_TR_obs.Setup_Joint_Model(Parameters, self.Types, 
                                                               self.J, self.Epsilon, Parameters['Obs_claims'])
        
    
    
    def exec(self, Parameters):
        
        if "observable" not in Parameters or Parameters["observable"] == "False":
            self.build_Epsilon(Parameters)
            self.build_model(Parameters)
        else:
            
            self.build_observable_model()
            
        
        

        if Parameters["irreducibility"]:
            self.base_backend.Constraint.Add_Irreducibility(self.model, Parameters["nbr_of_classes"], self.Types, periods= Parameters["periods"])
        
        if Parameters["profit"]:
            self.base_backend.Constraint.Add_Profit(self.model, Parameters["nbr_of_classes"], Parameters["Exp_claims"], Parameters["Ratio_of_types"],self.Types, periods = Parameters["periods"])

        if Parameters["one_class"]:
            self.base_backend.Constraint.Add_OwnPremiums(self.model, Parameters["nbr_of_classes"])
            
            
        #solve model
        self.base_backend.solve_model(self.model, Parameters["solver"], Parameters["consol"])
        
        

        if self.model.status == 1:
            self.Premiums = calculation.solution.optimal_premiums(self.model,  self.Epsilon, Parameters["nbr_of_classes"])
            self.Transition_rules = calculation.solution.optimal_TR(self.model, Parameters["rule_type"])
            
            self.Stat_probabilities = calculation.solution.convert_c_statvar(self.model,self.Types, Parameters["nbr_of_classes"], Parameters["periods"])
            self.OP = calculation.solution.OP_group(self.Stat_probabilities, self.Premiums, self.Types, Parameters["Exp_claims"], Parameters["Ratio_of_types"], Parameters)
            self.TOP = calculation.solution.total_OP(self.Stat_probabilities, self.Premiums, self.Types, Parameters["Exp_claims"], Parameters["Ratio_of_types"], Parameters)
 
            print(self.OP)


            consol.environment_print(self.model, Parameters["rule_type"], "time", "Obj", TR="TR", premiums = self.Premiums)  
            
        else:
            consol.print_status(self.model.status)
            util.empty_solution(self)

            
        
class Stationary_probabilities():
    def __init__(self, Parameters):
        """ constructor """
        self.J = [k for k in range(-Parameters["nbr_of_classes"]+1, Parameters["nbr_of_classes"])]  
        self.Types = [each for each in Parameters["Exp_claims"]]
        
        
        if Parameters["rule_type"] == "S":
            import backend_PulP_st_TR
            self.backend = backend_PulP_st_TR
        
    
    def exec(self, Parameters):

        self.model = self.backend.Setup_BasicFixedTRModel(Parameters, self.Types, self.J)
    
        #solve model
        self.backend.solve_model(self.model, Parameters["solver"], Parameters["consol"])  
        
        
       
        #consol.print_dictionary(self.Stat_probabilities, "Prob")

        if self.model.status == 1: #or self.model.status == 0:
            consol.environment_print(self.model, "time", "Obj")
            self.Premiums ={k : 0 for k in range(Parameters["nbr_of_classes"])}
            consol.print_statprob_var(self.model, self.Types, Parameters["nbr_of_classes"])

        else:
            consol.print_status(self.model.status)
    
        
        
        
        
        
class Optimise_premiums():
    def __init__(self, Parameters):
        """ constructor """
        self.J = [k for k in range(-Parameters["nbr_of_classes"]+1, Parameters["nbr_of_classes"])]  
        self.Types = [each for each in Parameters["Exp_claims"]]
        
        
        import backend_PulP_st_TR
        self.backend = backend_PulP_st_TR
        
    
    def build_StatProbabilities(self, Parameters):
        self.Stat_probabilities = self.backend.solve_stat_probabilities(Parameters, self.Types, self.J)
    
    def exec(self, Parameters):
                       
        self.build_StatProbabilities(Parameters)
        
        
        self.model = self.backend.Setup_Premium_Model(Parameters, self.Stat_probabilities, self.Types) 
        
           
        if Parameters["profit"]:
            self.backend.Constraint.Add_Profit(self.model, Parameters["nbr_of_classes"], Parameters["Exp_claims"], Parameters["Ratio_of_types"],self.Types, self.Stat_probabilities)

        #solve model
        self.backend.solve_model(self.model, Parameters["solver"], Parameters["consol"])         
        
        
        if self.model.status == 1:# or self.model.status == 0:
            self.Premiums = calculation.solution.optimal_premium_variables(self.model, Parameters["nbr_of_classes"])
            consol.environment_print(self.model, "S","time", "Obj", premiums = self.Premiums)

        else:
            consol.print_status(self.model.status)
        
        
        
        
        
        
        

class Optimise_TR():
    def __init__(self, Parameters):
        """ constructor """
        self.Types = [each for each in Parameters["Exp_claims"]]
        
        if Parameters["rule_type"] == "S":
            Optimise_joint.build_unified_rules(self, Parameters)

        else:
            Optimise_joint.build_nonunified_rules(self, Parameters)


    def build_model(self, Parameters):
        """set up the basic model"""
        self.model = self.backend.Setup_TR_Model(Parameters, self.Types, self.J)
    
    
    def exec(self, Parameters):
        
        self.build_model(Parameters)
        

        if Parameters["irreducibility"]:
            self.base_backend.Constraint.Add_Irreducibility(self.model, Parameters["nbr_of_classes"], self.Types)
        
        if Parameters["profit"]:
            self.base_backend.Constraint.Add_Profit_fixedPremiums(self.model, Parameters["nbr_of_classes"], Parameters["Exp_claims"], Parameters["Ratio_of_types"],self.Types)

        #solve model
        self.base_backend.solve_model(self.model, Parameters["solver"], Parameters["consol"])  
       
        

        if self.model.status == 1:# or self.model.status == 0:
            self.Stat_probabilities = calculation.solution.convert_c_statvar(self.model,self.Types, Parameters["nbr_of_classes"])

            consol.environment_print(self.model, Parameters["rule_type"], "time", "Obj", TR="TR", premiums = Parameters["Premiums"])    
            
        else:
            consol.print_status(self.model.status)
                   