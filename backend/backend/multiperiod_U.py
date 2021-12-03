# -*- coding: utf-8 -*-
"""
backend - multi period
"""

import pulp as pulp
import backend_PulP_st_TR

def Setup_Joint_Model(Parameters, Types, J, epsilon):
    """ Set_up the basic stationary model"""
    #redefine
    
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    Theta = Parameters["periods"]
    
    
    Jp = max(J)
    Jn = min(J)
    
    L = len(epsilon)
    

    # default premium
    pi = {k: min(Exp_claims.values()) for k in range(K+1)}    
    
    
    
    
    #variables
    ## Continous
    c = pulp.LpVariable.dicts("c", (range(K+1), Types, range(Theta+1)), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", (range(K+1), J, range(M+1), Types, range(Theta+1)), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]
    g = pulp.LpVariable.dicts("g", (range(K+1), Types, range(Theta+1)), lowBound = 0, cat ='Continous') #g[kategoria,csoport, idő]
    o = pulp.LpVariable.dicts("o", (range(K+1), range(L), Types, range(Theta+1)) , lowBound = 0, cat ='Continous') #op[kategoria,dijvaltoztatas,csoport]
    
    #Binary
    T = pulp.LpVariable.dicts("T", (J, range(M+1)), cat='Binary')
    O = pulp.LpVariable.dicts("O", (range(K+1), range(L)), cat='Binary')
    B = pulp.LpVariable.dicts("B", (range(K+1)), cat='Binary')
    
   


    #create model
    model = pulp.LpProblem("Multiperiod_MILP",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._c, model._d, model._g, model._o = c,d,g,o
    model._T, model._O = T, O
    model._pi, model._L = pi, L
    model._M, model._J = M, J
    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i][t] for k in range(K+1) for i in Types for t in range(Theta+1))


    #Constraints
    #Transition rules:
    backend_PulP_st_TR.Constraint.Add_TransitionRules(model, M, J , Jp, Jn, T)
    
    #stationary probabilities
    Constraint.Add_transitionProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T, Theta)
    
    
    #g-definition
    Constraint.Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, L, pi, c, o, g, Theta)
    

    #o-definition
    Constraint.Add_PremiumChangeDefinition(model,Types, K, L, epsilon, psi, o, c, O, Theta)
    
    #premium_rules
    backend_PulP_st_TR.Constraint.Add_PremiumConstraints(model, K, pi, epsilon, L, O)
    
        
    Constraint.Add_InitialClass(model, K, psi, Types, B, c)
    
    # model += T[1][0] == 1
    # model += T[-2][1] == 1
    
    
    return model


class Constraint:         
    def Add_transitionProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T, Theta):
        """Add the constraints to get  the stationarty distributions"""
    

        for t in range(Theta+1):
            #c_sum
            for i in Types:
                model += pulp.lpSum(c[k][i][t] for k in range(K+1))== psi[i], "c05_sumC_i"+str(i)+"_t"+str(t)

            #d definition
                for j in J:
                    for k in range(K+1):
                        for m in range(M+1):
                            model += d[k][j][m][i][t] >= Prob_of_claims[i,m] * c[k][i][t] - psi[i]*(1-T[j][m]),"c06_d_k"+str(k)+"_j"+str(j)+"_m" + str(m)+"_i"+str(i)+"_t"+str(t) 
                
        #c transitions
        for t in range(1,Theta+1):    
            for i in Types:    
                for k in range(1,K):
                    kezd = max(Jn, -(K-k))
                    veg = min(Jp,k)
                    model += c[k][i][t] == pulp.lpSum(d[k-j][j][m][i][t-1] for j in range(kezd, veg+1) for m in range(M+1)), "c09_trk_k"+str(k)+"_i"+str(i)+"_t"+str(t)
            
                model += c[K][i][t] == pulp.lpSum(d[K-l][j][m][i][t-1] for j in range(0, Jp+1) for l in range(0,j+1) for m in range(M+1)), "c10_trkK"+"_i"+str(i)+"_t"+str(t)
                model += c[0][i][t] == pulp.lpSum(d[0-l][j][m][i][t-1] for j in range(Jn, 1) for l in range(j,1) for m in range(M+1)), "c11_trk0"+"_i"+str(i)+"_t"+str(t)


   
    def Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, L, pi, c, o, g, Theta):
        """ Constraint to define the g-variable when the premium may change """
        for t in range(Theta+1):
            for i in Types:
                for k in range(K+1):
                    model += (pi[k]*c[k][i][t] + pulp.lpSum(o[k][l][i][t] for l in range(L))
                                    +g[k][i][t]
                                        >= Exp_claims[i]*c[k][i][t], "c14_g_elteres_p_k"+str(k)+"_i"+str(i)+"_t"+str(t))
                    model += (pi[k]*c[k][i][t] + pulp.lpSum(o[k][l][i][t] for l in range(L))
                                    -g[k][i][t]
                                        <= Exp_claims[i]*c[k][i][t], "c14b_g_elteres_n_k"+str(k)+"_i"+str(i)+"_t"+str(t))
            
            
            
    def Add_PremiumChangeDefinition(model,Types, K, L, epsilon, psi, o, c, O, Theta):
        """ define the premium change variable """
        
        #o definialasa
        for t in range(Theta+1):
            for i in Types:
                for k in range(K+1):
                    for l in range(L):
                        model += o[k][l][i][t] >= epsilon[l]*(c[k][i][t] - psi[i]*(1-O[k][l])), "c17a_op_also_k"+str(k)+"_l"+str(l) +"_i"+str(i)+"_t"+str(t)
                        model += o[k][l][i][t] <= epsilon[l]*c[k][i][t] , "c17b_op_felso_k"+str(k)+"_l"+str(l) +"_i"+str(i)+"_t"+str(t)
                        model += o[k][l][i][t] <= epsilon[l]*psi[i]*O[k][l], "c17c_op_bin_k"+str(k)+"_l"+str(l) +"_i"+str(i)+"_t"+str(t)             
            
        
        
    def Add_InitialClass(model, K, psi, Types, B, c):   
        """ constraints to define the initial class """
        
        model += pulp.lpSum(B[k] for k in range(K+1)) == 1, "c20_Boszt"
        
        for i in Types:
            for k in range(K+1):
                model+= c[k][i][0] == psi[i]*B[k], "c21_kezd_k"+str(k)+"_i"+str(i)     
            
        

