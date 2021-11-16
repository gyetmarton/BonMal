# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:58:05 2020

@author: gyetm
"""
import time
import consol
import calculation

import solve_model

import numpy as np

import backend_PulP_st_mTR
import backend_PulP_st_TR
import solver_parameters

import pulp
import copy


class Algo_iterative():
    """ Calculate the TR model, then the PR, then again TR, and so on..."""
    def __init__(self, Parameters):
        """ constructor """

        self.Types = [each for each in Parameters["Exp_claims"]]
        import backend_PulP_st_TR
        self.backend = backend_PulP_st_TR
        self.base_backend = backend_PulP_st_TR
        self.J = [k for k in range(-Parameters["nbr_of_classes"]+1, Parameters["nbr_of_classes"])]   

    
    def solve_TR_model(self, Parameters):
        """ build the TR model, then solve it and return the Objective the TRules and the stat probabilities """
        self.model = self.backend.Setup_TR_Model(Parameters, self.Types, self.J)
        
        
        if Parameters["irreducibility"]:
            self.base_backend.Constraint.Add_Irreducibility(self.model, Parameters["nbr_of_classes"], self.Types)
        
        if Parameters["profit"]:
            self.base_backend.Constraint.Add_Profit_fixedPremiums(self.model, Parameters["nbr_of_classes"], Parameters["Exp_claims"], Parameters["Ratio_of_types"],self.Types)

            
        self.base_backend.solve_model(self.model, Parameters["solver"]) 
        
                        
        if self.model.status == 1:
            self.Stat_probabilities = calculation.solution.convert_c_statvar(self.model,self.Types, Parameters["nbr_of_classes"])
            Transition_rules = calculation.solution.optimal_TR(self.model, Parameters["rule_type"])
            #Objective = self.model.objective.value()
            Objective = calculation.solution.objective_value(self.Stat_probabilities,Parameters["Premiums"], Parameters["Ratio_of_types"], Parameters["Exp_claims"], Parameters["round"])
            print("$$$$", Objective)
            consol.environment_print(self.model,  Parameters["rule_type"], "time", "Obj", TR="TR", premiums = None)  
           
        else:
            Stat_probabilities, Transition_rules, Objective = None, None, None
            consol.print_status(self.model.status)
        
        
        return Transition_rules, Objective
        
        
        
    def build_PR_model(self, Parameters):
        """ build the PR model, then solve it and return the Objective the Premiums"""
       
        self.model = self.backend.Setup_Premium_Model(Parameters, self.Stat_probabilities, self.Types) 
        
        
        if Parameters["profit"]:
            self.backend.Constraint.Add_Profit(self.model, Parameters["nbr_of_classes"], Parameters["Exp_claims"], Parameters["Ratio_of_types"],self.Types, self.Stat_probabilities)

        #solve model
        self.backend.solve_model(self.model, Parameters["solver"])       
        
        
        if self.model.status == 1:
            Premiums = calculation.solution.optimal_premium_variables(self.model, Parameters["nbr_of_classes"])
            #Objective = self.model.objective.value()
            Objective = calculation.solution.objective_value(self.Stat_probabilities,Premiums, Parameters["Ratio_of_types"], Parameters["Exp_claims"], Parameters["round"])
            print("$$$$", Objective)
            
            consol.environment_print(self.model, "S","time", "Obj", premiums = Premiums)
                        
        else:
            consol.print_status(self.model.status)
            Premiums, Objective = None, None
            
        return Premiums, Objective
    
    
    def exec(self, Parameters):
                
        start_time = time.time()
        objective_TR, objective_PR = 0, 1
        
        Obj_step = {}
        Diff_Obj_TR, Diff_Obj_TR2, Diff_Obj_TR3 ={},{},{}
        Diff_Obj_PR, Diff_Obj_PR2, Diff_Obj_PR3  = {}, {}, {}
        i = 0
        
        Diff_Obj_TR[-1],  Diff_Obj_TR2[-1], Diff_Obj_TR3[-1] =  -1, -1, -1
        Diff_Obj_PR[-1],  Diff_Obj_PR2[-1], Diff_Obj_PR3[-1] =  -1, -1, -1
        
        if Parameters["premium_type"] == "TRK":
            Parameters["Transition_rules"] = [1] +[-Parameters["nbr_of_classes"]+1 for m in range(Parameters["max_nbr_of_claims"]+1)]
        elif Parameters["premium_type"] == "TR1":
            Parameters["Transition_rules"] = [1] +[-1 for m in range(Parameters["max_nbr_of_claims"]+1)]
            
            
        if Parameters["premium_type"] in ["TRK", "TR1"]:
            self.Stat_probabilities = self.backend.solve_stat_probabilities(Parameters, self.Types, self.J)
        
        while (round(objective_TR,Parameters["round"])  != round(objective_PR,Parameters["round"])  and  
               Diff_Obj_TR[i-1] != 0 and Diff_Obj_TR2[i-1] != 0  and Diff_Obj_TR3[i-1] != 0 and 
               Diff_Obj_PR[i-1] != 0 and Diff_Obj_PR2[i-1] != 0  and Diff_Obj_PR3[i-1] != 0):
            
            if Parameters["premium_type"] in ["TRK", "TR1"]:
                #print("-->>",  self.Stat_probabilities)
                Parameters["Premiums"], objective_PR =  self.build_PR_model(Parameters)
                Transition_rules, objective_TR  = self.solve_TR_model(Parameters)
            else:
                #print("--ßß",   Parameters["Premiums"])
                Transition_rules, objective_TR  = self.solve_TR_model(Parameters)
                Parameters["Premiums"], objective_PR =  self.build_PR_model(Parameters)
            
            Obj_step[i] =  (objective_TR, objective_PR)
            
           
            if i >= 1:             
                Diff_Obj_TR[i] =  Obj_step[i][0] - Obj_step[i-1][0]
                Diff_Obj_PR[i] =  Obj_step[i][1] - Obj_step[i-1][1]
            else:
                Diff_Obj_TR[i] = -1
                Diff_Obj_PR[i] = -1
                
            if i >= 2:             
                Diff_Obj_TR2[i] =  Obj_step[i][0] - Obj_step[i-2][0]
                Diff_Obj_PR2[i] =  Obj_step[i][1] - Obj_step[i-2][1]
            else:
                Diff_Obj_TR2[i] = -1
                Diff_Obj_PR2[i] = -1
            
                        
            if i >= 3:             
                Diff_Obj_TR3[i] =  Obj_step[i][0] - Obj_step[i-3][0]
                Diff_Obj_PR3[i] =  Obj_step[i][1] - Obj_step[i-3][1]
            else:
                Diff_Obj_TR3[i] = -1
                Diff_Obj_PR3[i] = -1
            
            i += 1
            

            
            
            #objective_TR
            
        print("** approximation-steps: **")
        for each in Obj_step:            
            print(each,"--" ,  Obj_step[each], "----", Diff_Obj_TR[each], "<>", Diff_Obj_PR[each])
        running_time = time.time()-start_time
        
        print("\n")
        print("Time: ", running_time)
        print("Objective: ", objective_PR, "\n")
        
    
        return  objective_PR, Transition_rules, Parameters["Premiums"], running_time, i

class Algo_one_imp():
    """ Improves the unified transition rules with always one-change """
    
    def __init__(self, Parameters):
        """ constructor """
        
        self.Types = [each for each in Parameters["Exp_claims"]]

    def transform_TR_to_mTR(self, Parameters):
        """ Transform the initial solution to the nonunified form"""
        
        self.Best_Transition_rules = {k:{m:1 for m in range(Parameters["max_nbr_of_claims"]+1)} for k in range(Parameters["nbr_of_classes"])}
        
        for k in range(Parameters["nbr_of_classes"]):
            for m in range(Parameters["max_nbr_of_claims"]+1):  
                if k + self.init_Transition_rules[m] >= 0 and k + self.init_Transition_rules[m] < Parameters["nbr_of_classes"]:
                    self.Best_Transition_rules[k][m] = self.init_Transition_rules[m]
                elif k + self.init_Transition_rules[m] < 0:
                    self.Best_Transition_rules[k][m] =  -k 
                elif k + self.init_Transition_rules[m] >= Parameters["nbr_of_classes"]:
                    self.Best_Transition_rules[k][m] =   Parameters["nbr_of_classes"]-k-1    
        
       
    
    def build_J(self, Parameters):
        """ build the J where there can be +1/-1 changes """
    
        J, Jpp,Jpn, Jnp, Jnn= [], [], [], [], []
        
        
        for k in range(Parameters["nbr_of_classes"]):
            J.append([self.Best_Transition_rules[k][m] for m in range(Parameters["max_nbr_of_claims"]+1)])
            Jpp.append([self.Best_Transition_rules[k][m]+1 for m in range(Parameters["max_nbr_of_claims"]+1) 
                       if self.Best_Transition_rules[k][m]+k <Parameters["nbr_of_classes"]-1
                      and  self.Best_Transition_rules[k][m]>0])
            Jpn.append([self.Best_Transition_rules[k][m]+1 for m in range(Parameters["max_nbr_of_claims"]+1) 
                       if self.Best_Transition_rules[k][m] +1 <= 0 and  self.Best_Transition_rules[k][m]<0])
            
            Jnp.append([self.Best_Transition_rules[k][m]-1 for m in range(Parameters["max_nbr_of_claims"]+1)
                       if self.Best_Transition_rules[k][m] > 0 and self.Best_Transition_rules[k][m]-1>0])

            Jnn.append([self.Best_Transition_rules[k][m]-1 for m in range(Parameters["max_nbr_of_claims"]+1)
                       if self.Best_Transition_rules[k][m] <0 and 
                       k + self.Best_Transition_rules[k][m]-1 >= 0])

            J[k] = J[k] + Jpp[k] + Jpn[k] + Jnn[k] + Jnp[k]
            J[k] = list(dict.fromkeys(J[k]))
    
        self.J = J
    
    def solve_mTR_model(self, Parameters, best_objective, Transition_rules):
        """ setup model and solve it """
        Parameters["rule_type"] = "M"
        self.model = backend_PulP_st_mTR.Setup_TR_Model(Parameters, self.Types, self.J)
        
        #previos best solution
        obj_bound =  round(best_objective, 4)
        if round(best_objective, 4) < best_objective:
            obj_bound = round(best_objective+10**-4, 4)
        
        
        self.model += pulp.lpSum(Parameters["Ratio_of_types"][i]*self.model._g[k][i] for k in range(Parameters["nbr_of_classes"]) for i in self.Types) <= obj_bound
        
        
        
        if Parameters["irreducibility"]:
            backend_PulP_st_TR.Constraint.Add_Irreducibility(self.model, Parameters["nbr_of_classes"], self.Types)
        
        if Parameters["profit"]:
            backend_PulP_st_TR.Constraint.Add_Profit_fixedPremiums(self.model, Parameters["nbr_of_classes"], Parameters["Exp_claims"], Parameters["Ratio_of_types"],self.Types)

        #Set initial values for the transition rules
        
        for k in Transition_rules:
            for m in range(Parameters["max_nbr_of_claims"]+1):
                self.model._T[Transition_rules[k][m],m,k].setInitialValue(1)
        
        backend_PulP_st_TR.solve_model(self.model, Parameters["solver"])  
        
        print(">>", self.model.status)
        
        #print solution
        if self.model.status == 1 :
            self.Stat_probabilities = calculation.solution.convert_c_statvar(self.model,self.Types, Parameters["nbr_of_classes"], Parameters["periods"])
            consol.environment_print(self.model, Parameters["rule_type"], "time", "Obj", TR="TR", premiums = Parameters["Premiums"])    
            Transition_rules = calculation.solution.optimal_TR(self.model, Parameters["rule_type"])
            objective = self.model.objective.value()
        elif self.model.status == 0 and self.model.solverModel.SolCount>0:
            objective = self.model.solverModel.ObjVal 
            self.Stat_probabilities = {(k,i): v.x for k in range(Parameters["nbr_of_classes"]) for i in self.Types
                                       for v in self.model.solverModel.getVars() 
                                       if v.varName == "c_"+str(k)+"_"+str(i)}
            
            for k in range(Parameters["nbr_of_classes"]):
                for j in self.J[k]:
                    for m in range(Parameters["max_nbr_of_claims"]+1):
                        if self.model._T[j,m,k].varValue is None:
                            self.model._T[j,m,k].varValue = 0
            Transition_rules = calculation.solution.optimal_TR(self.model, Parameters["rule_type"])
        else:
            objective = best_objective
            print("There is no solution within the time limit!")
  
              
        return objective, Transition_rules

        
        
    def exec(self, Parameters):
        
        start_time = time.time()
        
        if Parameters["solver"] == "Gurobi":
            solver_parameters.pGurobi.Cutoff()
        
        #Initial solution
        Parameters["rule_type"] = "S"
        Optimisation = solve_model.Optimise_TR(Parameters)
        Optimisation.exec(Parameters)
        self.init_Transition_rules = calculation.solution.optimal_TR(Optimisation.model, Parameters["rule_type"])
        init_objective = Optimisation.model.objective.value()
        self.Stat_probabilities = Optimisation.Stat_probabilities
        
        # change the TR into MTR
        self.transform_TR_to_mTR(Parameters)
        
        best_objective = init_objective
        #Best_Transition_rules = self.init_Transition_rules
        # Change
     
        
        Optimal = False
        i = 0    
        while Optimal is False:
            i+=1
            self.build_J(Parameters)
            #if Parameters["solver"] == "Gurobi":
            #    solver_parameters.pGurobi.Cutoff(best_objective*1.01)
            objective, Transition_rules = self.solve_mTR_model(Parameters, best_objective, self.Best_Transition_rules)
            if objective < best_objective:
                best_objective = objective
                self.Best_Transition_rules = Transition_rules
            else:
                Optimal= True
                print(">>> solution found in ", i , "iteration!!!")
               

        
            
          
        Transition_rules = self.Best_Transition_rules
        
        running_time = time.time() - start_time
        
        print("IMPROVEMENT: ", (best_objective-init_objective)/init_objective)
        print("time: ", running_time)
        return best_objective, self.Best_Transition_rules, Parameters["Premiums"], running_time
        
        
class Algo_class_extreme():
    """ Improves the unified transition rules with always one-change """
    
    def __init__(self, Parameters):
        """ constructor """
        
        self.Types = [each for each in Parameters["Exp_claims"]]
        self.J = np.empty([Parameters["nbr_of_classes"], Parameters["nbr_of_classes"]], int)
        for k in range(Parameters["nbr_of_classes"]): 
            for s in range(Parameters["nbr_of_classes"]):
                    self.J[k][s] = -k+s
    
    
    def transform_transition_rule(TRule, max_nbr_of_claims, number_of_classes):
        """Transform the original model transition tule into the other format """
        Transition_rules = {}
        for claim in range(max_nbr_of_claims+1):
            for clss in range(number_of_classes):
                rule = TRule[claim]
                if rule + clss > number_of_classes-1:
                    rule = (number_of_classes-1) - clss
                elif rule + clss < 0:
                    rule = -clss
                Transition_rules[claim, clss] = rule
                
        return Transition_rules
     
    def Calculate_stat_probabilities(self, Parameters, Type, Transition_rules):
        """Calculate the stationary probabilities of a system, with the given transition rules """
            
        Claim_probabilities = {}
        for claim in range(Parameters["max_nbr_of_claims"]+1):
            Claim_probabilities[claim] = Parameters["Prob_of_claims"][Type, claim]
        
            
        Ones = np.ones((1, Parameters["nbr_of_classes"]))
        TPmatrix = np.zeros((Parameters["nbr_of_classes"], Parameters["nbr_of_classes"]))
        
        for clss in range(Parameters["nbr_of_classes"]):
            TPmatrix[clss][clss] = -1
            for claim in range(Parameters["max_nbr_of_claims"]+1):
                TPmatrix[clss + Transition_rules[clss][claim]][clss] += Claim_probabilities[claim]
        
        Left = np.r_[TPmatrix, Ones]
        Right = np.zeros(Parameters["nbr_of_classes"]+1)
        Right[Parameters["nbr_of_classes"]] = Parameters["Ratio_of_types"][Type]
        Stat_probabilities = np.linalg.lstsq(Left, Right, rcond=None)[0] 
                
        return Stat_probabilities
        
    def Calculate_Objective(self, Parameters, Transition_rules):
        """ calcuéate from the stationary probabilities the objective. """
        Stationary_probabilities = {}
        
        for Type in Parameters["Ratio_of_types"]:
            stat_prob_type = self.Calculate_stat_probabilities(Parameters, Type, Transition_rules)
            for clss in range(Parameters["nbr_of_classes"]):
                Stationary_probabilities[clss, Type] = stat_prob_type[clss]
        
        
        Objective = 0
        for clss in range(Parameters["nbr_of_classes"]):
            for Type in Parameters["Ratio_of_types"]:
                Objective += abs(Parameters["Premiums"][clss] * Stationary_probabilities[clss,Type] -  Parameters["Exp_claims"][Type] * Stationary_probabilities[clss,Type]) *Parameters["Ratio_of_types"][Type]
        return Objective, Stationary_probabilities
    
    def Local_search(self, clss, Parameters):
        max_nb = 1
        if clss == Parameters["nbr_of_classes"]-1:
            max_nb = 0
            
        min_nb = -1
        if clss == 0:
            min_nb = 0
        
        Objective, Stationary_probabilities = {}, {}
        for ls in range(min_nb, max_nb+1):
            
            if self.Best_Transition_rules[clss][1] + ls <= 0 and clss + self.Best_Transition_rules[clss][1] +ls >= 0:
                mod_Transition_rules = copy.deepcopy(self.Best_Transition_rules)
                mod_Transition_rules[clss][1] += ls
                
                Objective[ls], Stationary_probabilities[ls] = self.Calculate_Objective(Parameters, mod_Transition_rules)
        best_objective_change = min(Objective, key=Objective.get)
        best_objective = Objective[best_objective_change]
        Best_Stationary_probabilities = Stationary_probabilities[best_objective_change]
        
        Best_Transition_rules = copy.deepcopy(self.Best_Transition_rules)
        Best_Transition_rules[clss][1] += best_objective_change
        
        return Best_Transition_rules, best_objective, Best_Stationary_probabilities
        
  
    def exec(self, Parameters):
        
        start_time = time.time()
        
        #Initial solution
        Parameters["rule_type"] = "S"
        Optimisation = solve_model.Optimise_TR(Parameters)
        Optimisation.exec(Parameters)
        self.init_Transition_rules = calculation.solution.optimal_TR(Optimisation.model, Parameters["rule_type"])
        init_objective = Optimisation.model.objective.value()
        self.Stat_probabilities = Optimisation.Stat_probabilities
        
        Algo_one_imp.transform_TR_to_mTR(self, Parameters)
        
        best_objective = init_objective
        first_time = time.time()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("1st stage ready in ", round(first_time- start_time, 2), " seconds; Objective: ",  init_objective)   
        new_objective, objective_change, direction, class_TR_change, new_Stationary_probabilities  = {}, {}, {}, {}, {}
        Optimal = False
        k = 0
        while Optimal is False:
            print("\n>>")
            for clss in range(Parameters["nbr_of_classes"]):
                New_Transition_rules, new_objective[clss], new_Stationary_probabilities[clss] = self.Local_search(clss, Parameters)
               
            
                direction[clss] = np.sign(New_Transition_rules[clss][1]-self.Best_Transition_rules[clss][1])
                class_TR_change[clss] = New_Transition_rules[clss][1]
                if direction[clss] != 0:
                    objective_change[clss] = best_objective-new_objective[clss]
                else:
                    objective_change[clss] = 0
            
        
            for clss in new_objective:
                if objective_change[clss] > 0: 
                    print(clss, " > ", direction[clss], " > ", class_TR_change[clss], " > ", new_objective[clss], ">",best_objective )
                
            Optimal = not any(direction.values()) 
            
            if Optimal is False:
                change_class = min(new_objective, key=new_objective.get)
                print("## class", change_class, " change = ",  direction[change_class])
                self.Best_Transition_rules[change_class][1] = self.Best_Transition_rules[change_class][1] + direction[change_class]
                
                best_objective = new_objective[change_class]
                self.Stat_probabilities = new_Stationary_probabilities[change_class]
                
                print("Best objective: ", best_objective)
                k +=1 
            else:
                print("Optimal solution found in", time.time()- start_time)
            
        
        print("\n Optimal objective: ", best_objective, " steps",k ,"<<<", init_objective)
        
        

        
        print("\n")
        Parameters["rule_type"] = "M"
        running_time = time.time() - start_time
        print("IMPROVEMENT: ", (best_objective-init_objective)/init_objective)
        print("time: ", running_time)
        
        
        return best_objective, self.Best_Transition_rules, Parameters["Premiums"], running_time
                
        
        
        
        
        
