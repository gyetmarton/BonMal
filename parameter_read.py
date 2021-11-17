"""
 >> read parameters
"""

import json
import calculation
import tomli




def exec(parameter_file = 'parameter.toml', setup_folder = "."):
    #### Parameter import ####
    with open(parameter_file, "rb") as f:
        Parameters = tomli.load(f)
    
    
    
    # # with open(parameter_file) as f:
    # #     P = json.load(f)
    # #Setup
    # with open(setup_folder+'/setup/'+P["setup"]+'.json') as f:
    #     Parameters = json.load(f)


    #change the raw-parameters into usable parameters for the other parts.

    """number of classes"""
    Parameters["nbr_of_classes"] = P["nbr_of_classes"]
    

    
    """Probability of claims- number of claims"""
    Parameters["max_nbr_of_claims"] = P["max_nbr_of_claims"]
    
    
    Parameters["Prob_of_claims"] = setup.distribution(P, Parameters)
    
    
    """Add constraints"""
    Parameters["irreducibility"], Parameters["profit"], Parameters["one_class"]  = setup.additional_constraints(P)
    
    
    """ Model type """
    #Define the type of the model
    Parameters["model_type"] = P["model_type"]
    Parameters["Premiums"], Parameters["Transition_rules"] = setup.specific_parameter(P, Parameters)
    

    """ Transition rule type """    
    #S-Unified -- M --Not unified
    Parameters["rule_type"]  = P["rule_type"]


    Parameters["file_name"] = P["file_name"]
    """ Solver """   
    Parameters["solver"]  = P["solver"]

    """ multi-period-periods"""
    Parameters["periods"] = P["periods"]
    
    """ Approximation """
    if P["approx"] != 0:
        Parameters["approx"] = P["approx"]
    else:
        Parameters["approx"] = None
        
    Parameters["class_min"] = P["class_min"]    
    Parameters["class_max"] = P["class_max"]
    Parameters["premium_type"] = P["premium_type"]
    
    
    if P["consol"] == 0:
        Parameters["consol"] = False
    else:
        Parameters["consol"] = True
        
    
    Parameters["round"] = P["round"]
    
    
    return Parameters


class setup:
    def distribution(P, Data):
        """ setups the distribution of claims """
        if P["type_of_distribution"]=="d" and P["max_nbr_of_claims"] == 1:
            Prob_of_claims = calculation.distribution.Binary(Data['Exp_claims'])
        elif P["type_of_distribution"]=="pois" or (P["max_nbr_of_claims"] > 1):
            Prob_of_claims = calculation.distribution.Poisson(Data['Exp_claims'], P["max_nbr_of_claims"])
    
        return Prob_of_claims

    def additional_constraints(P):
        """ setuo fo the additional constrains """
            #irreducibility
        if "ir" in P["add_constraints"]:
            irreducibility = True
        else:
           irreducibility = False
            
        #profit constraint
        if "pr" in P["add_constraints"]:
            profit = True
        else:
            profit = False
        
        #one risk-group's fair-premium is the premium of at least one class' premium
        if "oc" in P["add_constraints"]:
            one_class = True
        else:
            one_class = False
        
        return irreducibility, profit, one_class
        
    def specific_parameter(P, Data):
        """ setup of the premiums when it is parameter and the transition rules when that is parameter..."""
        if P["model_type"] == "TR" or (P["model_type"] == "joint" and P["approx"]== "iter"):
            #set the premium parameter if the optimisation of the transition rules
            Transition_rules = None
            if P["premium_type"] == "prop":
               Premiums = calculation.premium.proportional_scale(P["nbr_of_classes"], Data["Ratio_of_types"], Data["Exp_claims"])
            elif P["premium_type"] == "lin":
               Premiums  = calculation.premium.linear_scale(P["nbr_of_classes"], Data["Exp_claims"])
            elif P["premium_type"] == "min":
               Premiums  = calculation.premium.min_almost(P["nbr_of_classes"], Data["Exp_claims"])
            elif P["premium_type"] == "max":
               Premiums  = calculation.premium.max_almost(P["nbr_of_classes"], Data["Exp_claims"])
            else:
                Premiums = 0
                Transition_rules = [0 for m in range(P["max_nbr_of_claims"]+1)]
            
        elif P["model_type"] == "PR" or  P["model_type"] == "stp":
            #set the transition rules for the optimisiation of premiums and the stationary probabilities calculations
            Premiums = None
            if P["max_nbr_of_claims"]+1 <= len(P["Transition_rules"]):
                Transition_rules = [P["Transition_rules"][m] for m in range(P["max_nbr_of_claims"]+1)]
            elif P["max_nbr_of_claims"]+1 > len(P["Transition_rules"]):
                Transition_rules = P["Transition_rules"] + [ P["Transition_rules"][-1] * (2+m) for m in range(P["max_nbr_of_claims"]+1-len(P["Transition_rules"]))]  
        else:
            Premiums, Transition_rules = None, None
            
            
        return Premiums, Transition_rules
    
    
    
    
    
    