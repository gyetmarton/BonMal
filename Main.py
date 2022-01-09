"""
Main program
-read parameters
-run optimisation
-print out solution and running time
"""

import util.parameter_read as parameter_read
import util.general as general
# import solver_parameters
import time

start_time = time.time()

# Import parameters
Parameters = parameter_read.exec()

# # Solve model
Result = general.run(Parameters)

print("time: ", round(time.time()-start_time, 2))


