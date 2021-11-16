# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:58:20 2020

@author: gyetm
"""

import general
import calculation
import pulp
import Output
import solver_parameters
import time





##§ Paraméterek
Exp_claims = { "A": 0.01,  "B": 0.05}
Ratio_of_types = { "A": 100,  "B": 100}

nbr_of_classes= 10

max_nbr_of_claims = 2

if max_nbr_of_claims == 1:
    Prob_of_claims = calculation.distribution.Binary(Exp_claims)
else:
    Prob_of_claims = calculation.distribution.Poisson(Exp_claims, max_nbr_of_claims)
  


solver = pulp.GUROBI()
#solver_parameters.set_default_parameters()
solver_parameters.set_basic_parameters()
solver_parameters.pGurobi.FeasibilityTol()
solver_parameters.pGurobi.MIPGap()


add_constraints = []
type_model = "stj"
#type_model = "prem"
start = 1 #ahonnan kezdenénk
maxtime  = 36000


File_name = "TTT.xlsx"#"Solution.xlsx"


classes = range(3,20)


Time, Obj = {},{}
TR, Premiums, OP = {}, {}, {}


start_time = time.time()


for k in classes:
    Transition_rules = [1,-5, -6]#-k+1]
    Time[k], Obj[k], TR[k], Premiums[k], OP[k] = general.run(k, max_nbr_of_claims, Exp_claims, Ratio_of_types, Prob_of_claims, 
                                          solver,
                        add_constraints, type_model, Transition_rules)
    current_time = time.time()-start_time
    print(">> Ready:   ", k, "--", current_time) 
    if current_time > maxtime:
        print("Time is up")
        break


   



"""
for each in Time:
    print(each, ">>", Time[each], ">>", Obj[each])
    print(TR[each], "---", Premiums[each])
"""   
    
###Save to code


Output.modWrite.write_MRun("M2_15", File_name, type_model, Obj, Time, OP, TR, Premiums,  
                           len(Ratio_of_types), max_nbr_of_claims, start = start)



