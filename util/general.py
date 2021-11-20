# -*- coding: utf-8 -*-
"""
This is the main of the interface. It is also callable function.
"""


#import Output
import util.solve_model as solve_model
import util.calculation as calculation
# import solve_approx


def run(Parameters):
    """ Run the optimisation models, with uniformed transition rules"""                
    
    Results = {}
    OP_calculation = True         
    
    if Parameters["model_type"] == "joint":    
        #Joint optimisation
        if Parameters["approx"] is None:
            Optimisation = solve_model.Optimise_joint(Parameters)
            Optimisation.exec(Parameters)
            #Calculate results
            
            Results["Transition_rules"] = Optimisation.Transition_rules 
            Results["Premiums"] =  Optimisation.Premiums
            
        # elif Parameters["approx"] == "iter":
        #     Optimisation = solve_approx.Algo_iterative(Parameters)
        #     Results["objective"], Results["Transition_rules"], Results["Premiums"], Results["running_time"], Results["iterations"] =  Optimisation.exec(Parameters)
        #     Optimisation.OP = calculation.solution.OP_group(Optimisation.Stat_probabilities, Results["Premiums"], Optimisation.Types, Parameters["Exp_claims"], Parameters["Ratio_of_types"], Parameters)
        #     Optimisation.TOP = calculation.solution.total_OP(Optimisation.Stat_probabilities, Results["Premiums"], Optimisation.Types, Parameters["Exp_claims"], Parameters["Ratio_of_types"], Parameters)
                
    elif Parameters["model_type"]  == "PR": 
        #Premium optimisation with fixed transition rules
        Optimisation = solve_model.Optimise_premiums(Parameters)
        Optimisation.exec(Parameters)
        Results["Premiums"] = Optimisation.Premiums
        Results["Transition_rules"] = Parameters["Transition_rules"]
     
    elif Parameters["model_type"]  == "TR":
        print(Parameters["approx"])
        if Parameters["approx"] is None:
            
            #Transition rule optimisation with fixed premiums
            Optimisation = solve_model.Optimise_TR(Parameters)
           
            
           
            
            Optimisation.exec(Parameters)
            Results["Premiums"] = Parameters["Premiums"]
            Results["Transition_rules"] = calculation.solution.optimal_TR(Optimisation.model, Parameters["rule_type"])
        # elif Parameters["approx"] == "one_imp":
        #     Optimisation = solve_approx.Algo_one_imp(Parameters)
        #     Results["objective"], Results["Transition_rules"], Results["Premiums"], Results["running_time"] = Optimisation.exec(Parameters)
        # elif Parameters["approx"] == "class_extreme":
        #     Optimisation = solve_approx.Algo_class_extreme(Parameters)
        #     Results["objective"], Results["Transition_rules"], Results["Premiums"], Results["running_time"] = Optimisation.exec(Parameters)
            
    
    elif Parameters["model_type"]  == "stp":
        Optimisation = solve_model.Stationary_probabilities(Parameters)
        Optimisation.exec(Parameters)
        OP_calculation = False
        Results["Premiums"] = Optimisation.Premiums
        Results["Transition_rules"] = Parameters["Transition_rules"]
    else:
        print("model name", Parameters["model_type"], "is unknown!!!")
        
     
     
    #Calculate results
    if OP_calculation:
        Results["OP"] = Optimisation.OP
        Results["TOP"] = Optimisation.TOP
    else:
        Results["OP"] = 0
        Results["TOP"] = 0
    
    """
    if Parameters["file_name"] is not None:
        Output.modWrite.write_ONE("PremiumOpt", Parameters["file_name"], Optimisation.model, Transition_rules, OP, Premiums,  
                                  len(Parameters["Ratio_of_types"]), Parameters["max_nbr_of_claims"], 1, 1)
    """
    
    # if Parameters["approx"] is None:
    #     #running_time = Optimisation.model.solutionTime 
    #     Results["running_time"] = time.time() - start_time
    #     Results["objective"] = Optimisation.model.objective.value()
     
        
    return  Results