# Bonus Malus optimizer

This is a program to optimize a Bonus-malus system (BMS). The description of the models is presented in my dissertation, Gyetvai, M.: Optimization of Bonus-Malus Systems.
To optimize a BMS, set up the parameter.tofl file, then run the Main.py. The program will find the optimal solution and write it to the consol. 


## List of files
#### Main folder
parameter.tofl - to set the parameters
Main.py - main file, read the parameters, and solve the model

#### backend 
stationer_U -  MILP model for the stationary models, with unified transition rules
stationer_NU - MILP model for the stationary models, with nonunified transition rules
multiperiod_U -  MILP model for the multiperiod models, with unified transition rules

#### util
calculation.py - consists functions for calculations
consol.py - functions to write the solution to the consol
general.py - selecting the model
parameter_read - read the parameters of parameter.tofl
solve_model - setups of the models and calls the required backend to solve it


## Usage
Set the parameters then run the Main.py

### Risk-groups parameters 
- **Exp_claims**: Dictionary of the expected claims of the risk-groups. (Eg., Exp_claims = { A = 0.01,  B = 0.02} - menas that we have two risk-groups, A and B with expected claim               of 0.01 and 0.02 respectively).
- **Ratio_of_types** :  Dictionary of the ratios of the risk-groups. It can mean the number of policyholders in the risk-groups as well (Eg., Exp_claims = Ratio_of_types =  { A = 50,  B = 50}).
- **max_nbr_of_claims**:  Maximal number of claims, should be greater than 0

### BMS parameters
- **nbr_of_classes**: Number of classes, should be greater than 1
- **rule_type**:  Type of the Transition rules (can be "U" (_uniformed_), or "NU" (_non-uniformed_))
- **model_type**: type of the model:
    -"joint" - joint optimisation of premiums and transition rules
    -"PR"    - optimisation of the premiums
    -"TR"    - optimisation of the transition rules
   -"stp"   - calculate the stationary probabilities of a transition rules
-**add_constraints**: Additional constraints to consider. The strings should be listed in [] separated with , (eg.: ["ir", "pr"])
    -"ir" - Adds an irreducibility constraint - all of the stationary probabilities should be greater than 10^9 (_can be added to model_type "joint" and "TR"_)
    -"pr" - Adds the profitability constraint (_can be added to model_type "joint", "TR" and "PR"_)
    -"oc" - Each risk-group's fair premiums should be presented in the premium-scale(_can be added to model_type "joint"_)

-**premium_type**: For the model_type "TR" sets the premium-scale
  - "lin"  - linear
  - "prop" - proportional to the ratios of the risk-groups
-**Transition_rules**:   For the model_type "PR" and "stp" set the Transition rule. It has to be a list, first element
is the 0-claim, then 1-claim, up to the "max_nbr_of_claims". (Eg. [1,-2, -4])
If there is less rules given (at least 2 element needed), then the twice of the last one considered
for the remaining claims."file_name": "optimal_solution.xlsx",
-**solver**: Set the solver for the model. Currently implemented:
- "Gurobi" (https://www.gurobi.com/)
- "GLPK" (https://www.gnu.org/software/glpk/)
- If anything else is used then the default is coin-Cbc (https://github.com/coin-or/Cbc)
"periods": Periods of time considered in the Multi-period optimisation. If it is 0, then the stationary model is considered.
The multi-period optimisation is only mplemented for the model_type "joint" with rule_type "S".
-"name": Name of the setup
-"Exp_claims": 


