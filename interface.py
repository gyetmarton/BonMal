# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:35:54 2020

Main interface, for one run

@author: gyetm
"""

#Interface
import argparse
#import solve_stac
import calculation
import pulp
import solver_parameters

import general

import json

#def main():
parser = argparse.ArgumentParser(description="Bonus_Malus optimisation")

parser.add_argument("-K", "--nbr_of_classes", type=int, 
                    help="The number of classes, if Kmin added, this is Kmax")

parser.add_argument("-Kmin", "--min_nbr_of_classes", type=int, 
                    help="The minimal number of classes, if iterate")

parser.add_argument("-Kstep", "--class_steps", type=int, 
                    help="The classes number-steps when iterate on the number of classes (empty = 1)")

parser.add_argument("-M", "--max_nbr_of_claims", type=int, 
                    help="The maximal number of claims per period")
     
parser.add_argument("-td", "--type_of_distribution", #metavar="ALGORITHM", 
                        help="type of distribution to use: \
                              binary-double [d]; \
                              poisson [pois]; ")    

parser.add_argument("-AC", "--add_constraints",  nargs="+", 
                        help="Add special constraint to the model:\
                        [ir]= irreducibility\
                        [pr]= profit\
                        [oc]= one type's premium in at least one class")
    
parser.add_argument("-mod", "--type_model",
                        help="Define the type of model:\
                        [joint]= stationer model joint\
                        [PR]= Heras' model\
                        [TR] = transition rule simple\
                        [stp] = Gives the stationary probabilities of given transition rules\
                        ")
                        
parser.add_argument("-ex", "--file_name",
                help="Save resoults to an excel file, add name")    

parser.add_argument("-data", "--data_file", 
                help="Add the json file-name from the parameters folder to call the parameters of the risk groups.")    

parser.add_argument("-T", "--TR", type=int,
                help="Add the transition rules of claims (claimless always 1).")    

parser.add_argument("-type", "--ruletype", 
                        help="type of BM model: \
                              Simple - One TR [S]; \
                              Multiple TR [M]; ")    
                              
                              
parser.add_argument("-app", "--approx", 
                        help="approximation: \
                              iterative  [iter]; \
                               ")    

parser.add_argument("-pi", "--premium_type", 
                        help="type of premium in the optimisation of the transition rules: \
                              proportional [prop]; \
                              linear [lin]; \
                               ")    
                                                          
                              
args = parser.parse_args()

with open('setup/'+args.data_file+'.json') as f:
  data = json.load(f)


Exp_claims = data['Exp_claims']
Ratio_of_types =  data['Ratio_of_types']




solver = pulp.GUROBI()
solver_parameters.set_basic_parameters()
#solver_parameters.set_default_parameters()
#solver_parameters.pGurobi.FeasibilityTol(1e-4)
solver_parameters.pGurobi.MIPGap()

Run = "Simple"


##Set the parameters from the args.   
if args.nbr_of_classes is not None:
    nbr_of_classes = args.nbr_of_classes
else:
    print("How much classes has the BM system?")

if args.min_nbr_of_classes is not None:
    if args.class_steps is not None:
        class_steps = args.class_steps
    else:
        class_steps = 1
        
    class_range = range(args.min_nbr_of_classes, nbr_of_classes, class_steps)
    Run = "Class_iterate"
    
    
if args.max_nbr_of_claims is not None:
    max_nbr_of_claims = args.max_nbr_of_claims
else:
    print("Add a maximal number of claims")

if args.type_of_distribution is not None and args.type_of_distribution not in ["d", "pois"]:
    print("unkown distribution\n")

if args.type_of_distribution=="d" or (max_nbr_of_claims == 1 and args.type_of_distribution is None):
    Prob_of_claims = calculation.distribution.Binary(Exp_claims)
elif args.type_of_distribution=="pois"or (max_nbr_of_claims > 1 and args.type_of_distribution is None):
    Prob_of_claims = calculation.distribution.Poisson(Exp_claims, max_nbr_of_claims)
  

if args.type_model is not None:
    type_model = args.type_model 
else:
    type_model = "joint"


if args.file_name is not None:
    file_name = args.file_name + ".xlsx"
else:
    file_name = None
    
    
if args.TR is not None:
    Transition_rules = [1,-args.TR]
else:
    
    Transition_rules = []
    Transition_rules.append(1)
    
    for m in range(1, 1+max_nbr_of_claims):
        Transition_rules.append(-nbr_of_classes+1)
    print(" ~~~ Transition rule: ", Transition_rules)


if args.ruletype is not None:
    ruletype = args.ruletype
else:
    ruletype = "S"



if args.approx is None:
    approx = None
else:
    approx = args.approx

add_constraints = args.add_constraints if args.add_constraints is not None  else []

   
if args.premium_type is not None:
    premium_type = args.premium_type 
else:
    premium_type = "prop"



"""RUN PROGRAM"""  

if Run == "Simple":   
    time, objective_value, Transition_rules, Premiums, OP, TOP = general.run_simple(nbr_of_classes, max_nbr_of_claims, Exp_claims, Ratio_of_types, Prob_of_claims,
                                                                        solver,
                                                                        add_constraints, type_model, Transition_rules, ruletype, premium_type, approx,  data, file_name)
    print(TOP)

elif Run == "Class_iterate":
    import K_iterate
    
    print("ASD")

