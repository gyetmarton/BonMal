# Bonus Malus optimizer

This is a program to optimize a Bonus-malus system (BMS). The description of the models is presented in my dissertation, Gyetvai, M.: Optimization of Bonus-Malus Systems
To optimize a BMS, set up the parameter.tofl file, then run the Main.py. The program will find the optimal solution and write it to the consol. 


## List of files

parameter.json - to set the parameters of the BMS
setup/setup.json - to set the parameters  of the policyholders
Main.py - main file, read the parameters, and solve the model
parameter_read - read the parameters of parameter.json and setup/setup.json
general.py - the selection of the model
solve_model - setups of the models and calls the required backend to solve it
calculation.py - consists functions for calculations
consol.py - functions to write the solution to the consol
backend_PulP_st_TR - backend- MILP model for the stationary models, with unified transition rules
backend_PulP_st_mTR - backend- MILP model for the stationary models, with nonunified transition rules
backend_PulP_mp_TR - backend- MILP model for the multiperiod models, with unified transition rules

## Usage
Set the parameters then run the Main.py

### description of parameters.json
-"setup": Name of the setup JSON-file, do not use the abbreviation.
-"nbr_of_classes": Number of classes, should be greater than 1
-"max_nbr_of_claims": Maximal number of claims, should be greater than 0
-"type_of_distribution": type of claim-distribution
- "d" - 0-1 claim-distribution
- "pois" - Poisson claim-distribution (if  "max_nbr_of_claims">1 then this distribution is used)
"model_type": type of the model:
-"joint" - joint optimisation of premiums and transition rules
-"PR"    - optimisation of the premiums
-"TR"    - optimisation of the transition rules
-"stp"   - calculate the stationary probabilities of a transition rules
-"add_constraints": Additional constraints to consider. The strings should be listed in [] separated with , (eg.: ["ir", "pr"])
-"ir" - Adds an irreducibility constraint - all of the stationary probabilities should be greater than 10^9
can be added to model_type "joint" and "TR"
-"pr" - Adds the profitability constraint
can be added to model_type "joint", "TR" and "PR"
-"oc" - Each risk-group's fair premiums should be presented in the premium-scale
can be added to model_type "joint"

"rule_type": Can be set how the transition rules are considered
-"S" -uniformed, every class has the same transition rules
-"M" -nonuniformed, the classes can have different transition rules
The "M" works only in the model_type "joint" or "TR", only in the stationary models
"premium_type": For the model_type "TR" sets the premium-scale
- "lin"  - linear
- "prop" - proportional to the ratios of the risk-groups
"Transition_rules":   For the model_type "PR" and "stp" set the Transition rule. It has to be a list, first element
is the 0-claim, then 1-claim, up to the "max_nbr_of_claims". (Eg. [1,-2, -4])
If there is less rules given (at least 2 element needed), then the twice of the last one considered
for the remaining claims."file_name": "optimal_solution.xlsx",
"solver": Set the solver for the model. Currently implemented:
- "Gurobi" (https://www.gurobi.com/)
- "GLPK" (https://www.gnu.org/software/glpk/)
- If anything else is used then the default is coin-Cbc (https://github.com/coin-or/Cbc)
"periods": Periods of time considered in the Multi-period optimisation. If it is 0, then the stationary model is considered.
The multi-period optimisation is only mplemented for the model_type "joint" with rule_type "S".
-"name": Name of the setup
-"Exp_claims": Dictionary of the expected claims of the risk-groups.
(Eg: { "A": 0.01,  "B": 0.05} - menas that we have two risk-groups, A and B with expected claim of 0.01 and 0.05 respectively).
-"Ratio_of_types":  Dictionary of the ratios of the risk-groups. It can mean the number of policyholders in the risk-groups as well.


