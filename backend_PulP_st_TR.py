# -*- coding: utf-8 -*-
"""
backend for simple TR stationary
"""

import pulp as pulp


def Setup_Joint_Model(Parameters, Types, J, epsilon):
    """ Set_up the basic stationary model"""
    #redefine
    
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    
    Jp = max(J)
    Jn = min(J)
    
    L = len(epsilon)
    

    # default premium
    pi = {k: min(Exp_claims.values()) for k in range(K+1)}    
    
    
    
    #variables
    ## Continous
    c = pulp.LpVariable.dicts("c", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", (range(K+1), J, range(M+1), Types), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]
    g = pulp.LpVariable.dicts("g", (range(K+1),Types), lowBound = 0, cat ='Continous') #g[kategoria,csoport, idő]
    o = pulp.LpVariable.dicts("o", (range(K+1), range(L), Types ) , lowBound = 0, cat ='Continous') #op[kategoria,dijvaltoztatas,csoport]

    #Binary
    T = pulp.LpVariable.dicts("T", (J, range(M+1)), cat='Binary')
    O = pulp.LpVariable.dicts("O", (range(K+1), range(L)), cat='Binary')


    #create model
    model = pulp.LpProblem("Stac_MILP",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._c, model._d, model._g, model._o = c,d,g,o
    model._T, model._O = T, O
    model._pi, model._L = pi, L
    model._M, model._J = M, J
    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i] for k in range(K+1) for i in Types)

    #Constraints
    #Transition rules:
    Constraint.Add_TransitionRules(model, M, J , Jp, Jn, T)

    #stationary probabilities
    Constraint.Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T)
    
    #g-definition
    Constraint.Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, L, pi, c, o, g)
    
    #o-definition
    Constraint.Add_PremiumChangeDefinition(model,Types, K, L, epsilon, psi, o, c, O)
    
    #premium_rules
    Constraint.Add_PremiumConstraints(model, K, pi, epsilon, L, O)

        
    return model

      
def Setup_BasicFixedTRModel(Parameters, Types, J):  
    """ Set_up and determine the stationary probabilities of each group .fixed transition rules"""
    #redefine
       
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    Transition_rules = Parameters["Transition_rules"]
        
    Jp = max(J)
    Jn = min(J)

    #Variables
    c = pulp.LpVariable.dicts("c", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", (range(K+1), J, range(M+1), Types), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]

    T = pulp.LpVariable.dicts("T", (J, range(M+1)), cat='Binary')
       
    #create model
    model = pulp.LpProblem("Stac_MILP",pulp.LpMinimize)

    model._c = c
    
    #The objective function 
    model += pulp.lpSum(T[j][0] for j in J) 

    
    # Constraints
    
    for m in range(M+1):
        model += T[Transition_rules[m]][m] ==1, "set_rule"+str(m)

    for m in range(M+1):
        model += pulp.lpSum(T[j][m] for j in J) ==1,  "c01_sumT_"+str(m)
    
    Constraint.Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T)
       
                    
    return model    
   
    
def Setup_Premium_Model(Parameters, Stat_probabilities, Types):   
    """"The modified Heras' model, with an objective function of each classes' deviations."""

    #Rename to the matematical abreviations
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]

    
    #Variables
    g = pulp.LpVariable.dicts("g", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport]
    pi = pulp.LpVariable.dicts("pi", (range(K+1)), lowBound = 0, cat ='Continous') #Pi_k

    #Objective function
    #create model
    model = pulp.LpProblem("Premium_Optimisation",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._g, model._pi = g, pi

    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i] for k in range(K+1) for i in Types)

    #Constraints
    for i in Types:
        for k in range(K+1):
            model += Stat_probabilities[k,i] * pi[k]+g[k][i] >=  Stat_probabilities[k,i] * Exp_claims[i] , "c01_UB"+str(k)+"_"+ str(i)   
            model += Stat_probabilities[k,i] * pi[k]-g[k][i] <=  Stat_probabilities[k,i] * Exp_claims[i] , "c02_LB"+str(k)+"_"+ str(i)

    for k in range(1, K+1):
        model += pi[k-1] >= pi[k], "c03"+str(k)
                   

    return model


def Setup_TR_Model(Parameters, Types, J):
    """ Set_up the basic stationary model for the Transition rules optimisation with fixed premiums"""

    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    pi = Parameters["Premiums"]
    
    Jp = max(J)
    Jn = min(J)

    # vaiables -cont
    c = pulp.LpVariable.dicts("c", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", (range(K+1), J, range(M+1), Types), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]
    g = pulp.LpVariable.dicts("g", (range(K+1),Types), lowBound = 0, cat ='Continous') #g[kategoria,csoport, idő]

    
    #binary
    T = pulp.LpVariable.dicts("T", (J, range(M+1)), cat='Binary')

    #create model
    model = pulp.LpProblem("Stac_MILP",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._c, model._d, model._g = c,d,g
    model._T,  model._pi = T, pi
    model._M, model._J = M, J
    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i] for k in range(K+1) for i in Types)


    
    ## Constraints
    Constraint.Add_TransitionRules(model, M, J , Jp, Jn, T)

    Constraint.Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T)
    
    Constraint.Add_AbsoluteVariableDefinition_NoChange(model, Types, K, Exp_claims, pi, c, g)
 
        
    return model

def solve_stat_probabilities(Parameters, Types, J):    
    
    model = Setup_BasicFixedTRModel(Parameters, Types, J)
        
    solve_model(model, Parameters["solver"])
    
    stat_var= {}
    for i in Types:
        for k in range(Parameters["nbr_of_classes"]):
            stat_var[k,i] =model._c[k][i].varValue
            
    return stat_var

def solve_model(model, solver, solver_msg=True):
    """ set the solver, solve it and alos writes the model into an .lp file"""    

    if solver == "Gurobi":
        model.setSolver(pulp.GUROBI(msg=solver_msg, warmStart=True))    
    elif solver == "GLPK":
        model.setSolver(pulp.GLPK())
    else:
        print("Default solver")
        model.setSolver()
        
    model.writeLP("modell.lp")  #create another function for this 

  
    model.solve()
    
    

class Constraint:  
    def Add_TransitionRules(model, M, J , Jp, Jn, T):
        """ Add the constraints to get an acceptable trasition rules """
        #1 claim-> 1 transition rule
        for m in range(M+1):
            model += pulp.lpSum(T[j][m] for j in J) ==1,  "c01_sumT_"+str(m)
    
        #positive, when m = 0
        model += pulp.lpSum(T[j][0] for j in range(1,Jp+1)) ==1, "c02_Tpos"
    
        #M-> negative  
        model += pulp.lpSum(T[j][M] for j in range(Jn, 0)) == 1, "c03_Tneg"
      
        #more claim more fall
        for m in range(M):
            for j in J:
                model += pulp.lpSum(T[l][m] for l in range(j, Jp+1)) >= T[j][m+1], "c04_TRdecr_j" +str(j)+"_m" +str(m)
        
    def Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T):
        """Add the constraints to get  the stationarty distributions"""
        for i in Types:
            #c_sum
            model += pulp.lpSum(c[k][i] for k in range(K+1))== psi[i], "c05_sumC_i"+str(i)
    
            #d definition
            for j in J:
                for k in range(K+1):
                    for m in range(M+1):
                        model += d[k][j][m][i] >=  Prob_of_claims[i,m] * c[k][i] - psi[i]*(1-T[j][m]),"c06_d_k"+str(k)+"_j"+str(j)+"_m" + str(m)+"_i"+str(i) 
                
            #c transitions
            for k in range(1,K):
                kezd = max(Jn, -(K-k))
                veg = min(Jp,k)
                model += c[k][i] == pulp.lpSum(d[k-j][j][m][i] for j in range(kezd, veg+1) for m in range(M+1)), "c09_trk_k"+str(k)+"_i"+str(i)
    
            model += c[K][i] == pulp.lpSum(d[K-l][j][m][i] for j in range(0, Jp+1) for l in range(0,j+1) for m in range(M+1)), "c10_trkK"+"_i"+str(i)
            model += c[0][i] == pulp.lpSum(d[0-l][j][m][i] for j in range(Jn, 1) for l in range(j,1) for m in range(M+1)), "c11_trk0"+"_i"+str(i)
       
    def Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, L, pi, c, o, g):
        """ Constraint to define the g-variable when the premium may change """
        for i in Types:
            #g deviation  
            for k in range(K+1):
                model += (pi[k]*c[k][i] + pulp.lpSum(o[k][l][i] for l in range(L))
                            +g[k][i]
                                    >= Exp_claims[i]*c[k][i], "c14_g_elteres_p_k"+str(k)+"_i"+str(i))
                model += (pi[k]*c[k][i] + pulp.lpSum(o[k][l][i] for l in range(L))
                            -g[k][i]
                                    <= Exp_claims[i]*c[k][i], "c14b_g_elteres_n_k"+str(k)+"_i"+str(i))
      
    def Add_AbsoluteVariableDefinition_NoChange(model, Types, K, Exp_claims, pi, c, g):
        """ Constraint to define the g-variable when the premium cannot change """
        for i in Types:                  
            #g deviation  
            for k in range(K+1):
                model += (pi[k]*c[k][i] +g[k][i]
                                    >= Exp_claims[i]*c[k][i], "c14_g_elteres_p_k"+str(k)+"_i"+str(i))
                model += (pi[k]*c[k][i] -g[k][i]
                                    <= Exp_claims[i]*c[k][i], "c14b_g_elteres_n_k"+str(k)+"_i"+str(i))
                    
    def Add_PremiumChangeDefinition(model,Types, K, L, epsilon, psi, o, c, O):
        """ define the premium change variable """
        for i in Types:
            for k in range(K+1):
                for l in range(L):
                    model += o[k][l][i] >= epsilon[l]*(c[k][i] - psi[i]*(1-O[k][l])), "c17a_op_also_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                    model += o[k][l][i] <= epsilon[l]*c[k][i] , "c17b_op_felso_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                    model += o[k][l][i] <= epsilon[l]*psi[i]*O[k][l], "c17c_op_bin_k"+str(k)+"_l"+str(l) +"_i"+str(i)
        
    def Add_PremiumConstraints(model, K, pi, epsilon, L, O):
        """ Constraint on the optimal premiums: """
        for k in range(K+1):
            
            #one class has one premium-change at most
            model+= pulp.lpSum(O[k][l] for l in range(L)) <= 1, "c18_egyvalt"+str(k)
        #monotonicity
        for k in range(K):
            model += ( pulp.lpSum(epsilon[l]*O[k][l] for l in range(L))
                    >= pulp.lpSum(epsilon[l]*O[k+1][l] for l in range(L)), "c16_dijmon_k"+str(k))    
       
    def Add_Irreducibility(model,nbr_of_classes,Types, periods = 0):
        #Add the irreducibility constraint
        if periods == 0:
            for k in range(nbr_of_classes):
                model += pulp.lpSum(model._c[k][i] for i in Types) >= 10**-9, "c12_irred_"+str(k)
        else:
            for k in range(nbr_of_classes):
                model += pulp.lpSum(model._c[k][i][periods] for i in Types) >= 10**-9, "c12_irred_"+str(k)
    
    def Add_Profit(model, nbr_of_classes, Exp_claims, Ratio_of_types, Types, Stat_probabilities = None, periods = 0):
        #Add the profitability constraint.
        if Stat_probabilities is None:
            if periods == 0:
                model += (pulp.lpSum(model._pi[k]*model._c[k][i] + pulp.lpSum(model._o[k][l][i] for l in range(model._L))
                            for i in Types for k in range(nbr_of_classes)) >= pulp.lpSum(Ratio_of_types[i]*Exp_claims[i] for i in Types), "c13_profit") 
            else:
                for t in range(periods+1):
                    model +=(pulp.lpSum(model._pi[k]*model._c[k][i][t]+ pulp.lpSum(model._o[k][l][i][t] for l in range(model._L))
                            for i in Types for k in range(nbr_of_classes)) >= pulp.lpSum(Ratio_of_types[i]*Exp_claims[i] for i in  Types), "c13_profit"+"_t"+str(t))  
        else:
            model += (pulp.lpSum(Stat_probabilities[k,i] * model._pi[k] for i in Types for k in range(nbr_of_classes)) 
                      >= pulp.lpSum(Ratio_of_types[i]*Exp_claims[i] for i in Types), "c13_profit") 
    
    
    def Add_Profit_fixedPremiums(model, nbr_of_classes, Exp_claims, Ratio_of_types,Types):
        #Add the profitability constraint. when the premium is fixed
            
        model += (pulp.lpSum(model._pi[k]*model._c[k][i] for i in Types for k in range(nbr_of_classes)) 
                  >= pulp.lpSum(Ratio_of_types[i]*Exp_claims[i] for i in Types), "c13_profit")
    
    
    def Add_OwnPremiums(model, nbr_of_classes):
        """Add a constraint that each types own premium should appear in the optimal solution."""
        #minimal-layer-at least one:
        model += (pulp.lpSum(model._O[k][l] for k in range(nbr_of_classes) for l in range(model._L)) <= nbr_of_classes-1, 
                  "c19_OWN_min")
        
        #every others:
        for l in range(model._L):
            model += (pulp.lpSum(model._O[k][l] for k in range(nbr_of_classes)) >= 1, "c19_OWN_max" +str(l))


