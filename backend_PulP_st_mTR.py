# -*- coding: utf-8 -*-
"""
backend for muti-TR stationary
"""

import pulp as pulp
import numpy as np
import backend_PulP_st_TR

def Setup_Joint_Model(Parameters, Types, J, epsilon):
    """ Set_up the basic stationary model with multi_transition rules"""
    #redefine
    
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    
    
    Jn = np.empty([K+1], int)
    Jp = np.empty([K+1], int)    
    for k in range(K+1):
        Jp[k] = K-k
        Jn[k] = -k
    
    
    L = len(epsilon)
    
    # default premium
    pi = {k: min(Exp_claims.values()) for k in range(K+1)}    
    
    
    #variables
    ## Continous
    c = pulp.LpVariable.dicts("c", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", ((k, j, m, i) for k in range(K+1) for j in J[k] for m in range(M+1) for i in Types), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]
    g = pulp.LpVariable.dicts("g", (range(K+1),Types), lowBound = 0, cat ='Continous') #g[kategoria,csoport, idő]
    o = pulp.LpVariable.dicts("o", (range(K+1), range(L), Types ) , lowBound = 0, cat ='Continous') #op[kategoria,dijvaltoztatas,csoport]

    #Binary
    T = pulp.LpVariable.dicts("T", ((j,m,k) for k in range(K+1) for j in J[k] for m in range(M+1)), cat='Binary')
    O = pulp.LpVariable.dicts("O", (range(K+1), range(L)), cat='Binary')

    #create model
    model = pulp.LpProblem("Stac_MILP",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._c, model._d, model._g, model._o = c,d,g,o
    model._T, model._O = T, O
    model._pi, model._L = pi, L
    model._M, model._J,  model._K = M, J, K
    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i] for k in range(K+1) for i in Types)


    #Constraints
    #Transition rules:
    Constraint.Add_TransitionRules(model, K, M, J, T)

    #stationary probabilities
    Constraint.Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T)
    
    #g-definition
    backend_PulP_st_TR.Constraint.Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, L, pi, c, o, g)
    
    #o-definition
    backend_PulP_st_TR.Constraint.Add_PremiumChangeDefinition(model,Types, K, L, epsilon, psi, o, c, O)
    
    #premium_rules
    backend_PulP_st_TR.Constraint.Add_PremiumConstraints(model, K, pi, epsilon, L, O)

    

   
    return model

class Constraint:  
    def Add_TransitionRules(model, K, M, J, T):
        """ Add the constraints to get an acceptable trasition rules """
                
        for k in range(K+1):
            for m in range(M+1):
                model += pulp.lpSum(T[j,m,k] for j in J[k]) ==1,  "c01_sumT_"+str(m)+"k"+str(k)
        
            #0-claim pozitive
            if k<K:
                model += pulp.lpSum(T[j,0,k] for j in J[k] if j>= 1) ==1, "c02_Tpos"+"k"+str(k)
            else:
                model += pulp.lpSum(T[j,0,k] for j in J[k] if j>= 0) ==1, "c02_Tpos"+"k"+str(k)
            
            #Largest claim is negative
            if k >0:
                model += pulp.lpSum(T[j,M,k] for j in J[k] if j < 0) == 1, "c03_Tneg"+"k"+str(k)
            else:
                model += pulp.lpSum(T[j,M,k] for j in J[k] if j < 1) == 1, "c03_Tneg"+"k"+str(k)
    
            #More claim - more fall
            for m in range(M):
                for j in J[k]:
                    model += pulp.lpSum(T[l,m,k] for l in J[k] if l >j ) >= T[j,m+1,k], "c04_TRdecr_j" +str(j)+"_m" +str(m)+"k"+str(k)


        
    def Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T):
        """Add the constraints to get  the stationarty distributions"""
   
        for i in Types:
            #c_sum
            model += pulp.lpSum(c[k][i] for k in range(K+1))== psi[i], "c05_sumC_i"+str(i)
    
            #d definition
            for k in range(K+1):
                for j in J[k]:
                    for m in range(M+1):
                        model += d[k,j,m,i] >= Prob_of_claims[i,m] * c[k][i] - psi[i]*(1-T[j,m,k]),"c06_d_k"+str(k)+"_j"+str(j)+"_m" + str(m)+"_i"+str(i) 
             
                #c transitions
                kezd = -(K-k)
                veg = k
                model += c[k][i] == pulp.lpSum(d[k-j,j,m,i] for j in range(kezd, veg+1)  if j in J[k-j] for m in range(M+1)), "c09_trk_k"+str(k)+"_i"+str(i)
    
                


      
def Setup_TR_Model(Parameters, Types, J):
    """ Set_up the basic stationary model for the Transition rules optimisation with fixed premiums"""
    
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    pi = Parameters["Premiums"]



    Jn = np.empty([K+1], int)
    Jp = np.empty([K+1], int)    
    for k in range(K+1):
        Jp[k] = max(J[k])#K-k
        Jn[k] = min(J[k])#-k
         

        

    # vaiables -cont
    c = pulp.LpVariable.dicts("c", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", ((k, j, m, i) for k in range(K+1) for j in J[k] for m in range(M+1) for i in Types), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]
    g = pulp.LpVariable.dicts("g", (range(K+1),Types), lowBound = 0, cat ='Continous') #g[kategoria,csoport, idő]

    #binary
    T = pulp.LpVariable.dicts("T", ((j,m,k) for k in range(K+1) for j in J[k] for m in range(M+1)), cat='Binary')
    

    #create model
    model = pulp.LpProblem("Stac_MILP",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._c, model._d, model._g = c,d,g
    model._T, model._pi = T, pi
    model._M, model._J, model._K = M, J, K
    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i] for k in range(K+1) for i in Types)

        
    ## Constraints
    Constraint.Add_TransitionRules(model, K, M, J, T)

    Constraint.Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T)
    
    backend_PulP_st_TR.Constraint.Add_AbsoluteVariableDefinition_NoChange(model, Types, K, Exp_claims, pi, c, g)
            
            
            
       
    return model


def Add_Fix_Transition_rules(model, nbr_of_classes, class_exclude, Transition_rules):
    #Fix the transition rules only enable the change for the classes thate we exclude
    
    for each in Transition_rules:
        if  each[1] != class_exclude:
            model += model._T[(Transition_rules[each],)+each] == 1, "D_fix_m"+ str(each[0])+"k"+ str(each[1])+ "TR"+ str(Transition_rules[each])
        
    
def Add_positive_one_claimless(model):
    #The transition rule for the claimless case is 1.
    
    for clss in range(model._K):
        model += model._T[1, 0, clss] == 1, "D_pos"+ str(clss)

