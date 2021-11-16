"""
Main program
-read parameters
-run optimisation
-print out solution and running time
"""

import parameter_read
import general
import solver_parameters
import time


start_time = time.time()


#solver_parameters.pGurobi.Timelimit(value = 3600*10)
#solver_parameters.pGurobi.ConsolOutput(1)

# Import parameters
Parameters = parameter_read.exec()

# # Solve model
# Result = general.run_simple(Parameters)

print("time: ", round(time.time()-start_time, 2))


# for each in Result:
#     print(each, Result[each])


#print(OP)


