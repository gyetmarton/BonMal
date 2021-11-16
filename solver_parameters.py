import gurobipy 




class  pGurobi:
    def NodefileStart(value):
        gurobipy.setParam("NodefileStart", value)
        
    def NodefileDir(path):
        gurobipy.setParam("NodefileDir", path)  
        
    def Method(value = -1):
        gurobipy.setParam("Method", value)
        """
        Minimum value:	-1
        Maximum value:	5
        Algorithm used to solve continuous models or the root node of a MIP model. 
        Options are: -1=automatic, 0=primal simplex, 1=dual simplex, 2=barrier, 3=concurrent, 4=deterministic concurrent, 
        5=deterministic concurrent simplex.
        """
        
    def Cutoff(value = 1e+100):
        gurobipy.setParam("Cutoff", value)
        
    def Timelimit(value = 1e+100):
        gurobipy.setParam("TimeLimit", value)

    def IntFeasTol(value = 1e-5):
        gurobipy.setParam("IntFeasTol", value)
        """
         Integer feasibility tolerance
             Min value:	1e-9
             Max value:	1e-1
         An integrality restriction on a variable is considered satisfied when the variable's value is 
         less than IntFeasTol from the nearest integer value. 
         Tightening this tolerance can produce smaller integrality violations, but very tight tolerances may significantly 
         increase runtime. Loosening this tolerance rarely reduces runtime.
         
        """

    
    def FeasibilityTol(value = 1e-6):
        gurobipy.setParam("FeasibilityTol", value)
        """
        Primal feasibility tolerance
            Min value:	1e-9
            Max value:	1e-2
            All constraints must be satisfied to a tolerance of FeasibilityTol. 
            Tightening this tolerance can produce smaller constraint violations, but for numerically challenging models 
            it can sometimes lead to much larger iteration counts.
        """
   
     
    
    def MIPGap(value = 1e-4):
         gurobipy.setParam("MIPGap", value)
         """
         Relative MIP optimality gap
     	 	Min value:	0
            Max value:	Infinity
            The MIP solver will terminate (with an optimal result) when the gap between the lower and upper
            objective bound is less than MIPGap times the absolute value of the upper bound.
         """
     
    def ConsolOutput(value):
        """
        If the value is 1, the output is written in the console, if it is 0, then it is not.
        """
        gurobipy.setParam("OutputFlag", value)
         

        


def set_default_parameters():
    pGurobi.Method()
    pGurobi.IntFeasTol()
    pGurobi.Cutoff()
    pGurobi.Timelimit()
    pGurobi.FeasibilityTol()
    pGurobi.MIPGap()
    

def set_basic_parameters(path = 'D://Gurobinodes'):
    pGurobi.NodefileStart(0.7)
    pGurobi.NodefileDir(path)
    pGurobi.Method(3)
    pGurobi.IntFeasTol(1e-09)
    pGurobi.FeasibilityTol(value = 1e-6)
    pGurobi.MIPGap(1e-4)
