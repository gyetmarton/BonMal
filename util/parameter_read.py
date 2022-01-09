"""
 >> read parameters
"""

import util.calculation as calculation
import tomli




def exec(parameter_file = 'parameter.toml', setup_folder = "."):
    #### Parameter import ####
    with open(parameter_file, "rb") as f:
        Parameters = tomli.load(f)
    
    #Calculate the claim number distribution   
    Parameters["Prob_of_claims"] = setup.distribution(Parameters)
    
    
    # """Add constraints"""
    Parameters["irreducibility"], Parameters["profit"], Parameters["one_class"]  = setup.additional_constraints(Parameters)
    
    # """ Model type """
    # #Define the type of the model
    Parameters["Premiums"], Parameters["Transition_rules"] = setup.specific_parameter(Parameters)
    

    # """ Transition rule type """    
    # #S-Unified -- M --Not unified
    if Parameters["rule_type"] == "NU":
        Parameters["rule_type"] = "M"
    else:
        Parameters["rule_type"] = "S"
    
    # """ Approximation """
    if Parameters["approx"] == 0:
        Parameters["approx"] = None
        
    if Parameters["consol"] == 0:
        Parameters["consol"] = False
    else:
        Parameters["consol"] = True

    if Parameters["observable"] == "True" or Parameters["observable"] == "T":
        Parameters["observable"] = True
    else:
        Parameters["observable"] = False        
    
    return Parameters


class setup:
    def distribution(Parameters):
        """ setups the distribution of claims - if there can happen multiple claims, then it is Poisson distribution """
        
        if Parameters["max_nbr_of_claims"] == 1:
            Prob_of_claims = calculation.distribution.Binary(Parameters['Exp_claims'])
        elif Parameters["max_nbr_of_claims"] > 1:
            Prob_of_claims = calculation.distribution.Poisson(Parameters['Exp_claims'], Parameters["max_nbr_of_claims"])
    
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
        
    def specific_parameter(P):
        """ setup of the premiums when it is parameter and the transition rules when that is parameter..."""
        if P["model_type"] == "TR" or (P["model_type"] == "joint" and P["approx"]== "iter"):
            #set the premium parameter if the optimisation of the transition rules
            Transition_rules = None
            if P["premium_type"] == "lin":
               Premiums  = calculation.premium.linear_scale(P["nbr_of_classes"], P["Exp_claims"])
            elif P["premium_type"] == "min":
               Premiums  = calculation.premium.min_almost(P["nbr_of_classes"], P["Exp_claims"])
            elif P["premium_type"] == "max":
               Premiums  = calculation.premium.max_almost(P["nbr_of_classes"], P["Exp_claims"])
            else:
                Premiums = calculation.premium.proportional_scale(P["nbr_of_classes"], P["Ratio_of_types"], P["Exp_claims"])
            
        elif P["model_type"] == "PR" or  P["model_type"] == "stp":
            #set the transition rules for the optimisiation of premiums and the stationary probabilities calculations
            Premiums = None
            if P["max_nbr_of_claims"]+1 <= len(P["Transition_rules"]):
                Transition_rules = [P["Transition_rules"][m] for m in range(P["max_nbr_of_claims"]+1)]
            elif P["max_nbr_of_claims"]+1 > len(P["Transition_rules"]):
                Transition_rules = P["Transition_rules"] + [ P["Transition_rules"][-1] * (2+m) for m in range(P["max_nbr_of_claims"]+1-len(P["Transition_rules"]))]  
            
            
            #limit the negative steps
            Transition_rules = [min(max(rule, - (P["nbr_of_classes"]-1)),P["nbr_of_classes"]-1)  for rule in Transition_rules]
           
            print(Transition_rules)
        
        else:
            Premiums, Transition_rules = None, None
            
            
        return Premiums, Transition_rules
    
    
    
    
    
    