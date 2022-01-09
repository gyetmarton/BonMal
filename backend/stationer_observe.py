# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:41:30 2020

@author: gyetm

for simple TR stationary with observable risks
"""

import pulp as pulp
import backend.stationer_U as backend


def Setup_Joint_Model(Parameters, Types, J, epsilon):
    """ Set_up the basic stationary model"""
    #redefine
    
    
    K = Parameters["nbr_of_classes"]-1
    M = Parameters["max_nbr_of_claims"]
    psi = Parameters["Ratio_of_types"]
    Exp_claims = Parameters["Exp_claims"]
    Prob_of_claims = Parameters["Prob_of_claims"]
    Obs_claims = Parameters["Obs_claims"]
     
 
    
    
    
    Jp = max(J)
    Jn = min(J)
    
    L = len(epsilon)
    
    Lp = 0
    Ln = 0
    L_var = {}
    epsilon_p, epsilon_n = [], []
    for num, each in enumerate(epsilon):
        if each > 0:
            L_var[num] = Lp
            epsilon_p.append(each) 
            Lp += 1
        else:
            L_var[num] = Ln
            epsilon_n.append(each)
            Ln += 1
            
    print("poz_changes: ", epsilon_p,">> neg_changes: " , epsilon_n)

    ###################
    ## ELŐKÉSZÜLETEK ##
    ###################
    pi = {k: 0 for k in range(K+1)}    
    
    
    ##############
    ## VÁLTOZÓK ##
    ##############

    ## Folytonos
    c = pulp.LpVariable.dicts("c", (range(K+1),Types), lowBound = 0, cat ='Continous') #c[kategoria,csoport, idő]
    d = pulp.LpVariable.dicts("d", (range(K+1), J, range(M+1), Types), lowBound = 0, cat ='Continous') #d[kategoria,lepes,karszam,csoport, idő]
    g = pulp.LpVariable.dicts("g", (range(K+1),Types), lowBound = 0, cat ='Continous') #g[kategoria,csoport, idő]
    op = pulp.LpVariable.dicts("op", (range(K+1), range(Lp), Types) , lowBound = 0, cat ='Continous') #op[kategoria,dijvaltoztatas,csoport]
    on = pulp.LpVariable.dicts("on", (range(K+1),  range(Ln), Types), lowBound = 0, cat ='Continous') #op[kategoria,dijvaltoztatas,csoport]

    
    #Bináris
    T = pulp.LpVariable.dicts("T", (J, range(M+1)), cat='Binary')
    O = pulp.LpVariable.dicts("O", (range(K+1), range(L)), cat='Binary')
    Op = pulp.LpVariable.dicts("Op", (range(K+1), range(Lp)), cat='Binary')
    On = pulp.LpVariable.dicts("On", (range(K+1), range(Ln)), cat='Binary')

       
    #################
    ## CÉLFÜGGVÉNY ##
    #################
    #create model
    model = pulp.LpProblem("Stac_MILP",pulp.LpMinimize)

    #stick variables to 'model', to retreieve these later
    model._c, model._d, model._g, model._op,  model._on= c,d,g,op, on
    model._T, model._Op, model._On = T, Op, On
    model._pi, model._L = pi, L
    model._M, model._J = M, J
    
    model._O = O
    
    #The objective function 
    model += pulp.lpSum(psi[i]*g[k][i] for k in range(K+1) for i in Types)


    ##############
    ## KORLÁTOK ##
    ##############
  
    #Transition rules:
    backend.Constraint.Add_TransitionRules(model, M, J , Jp, Jn, T)

    #stationary probabilities
    backend.Constraint.Add_StationaryProbabilities(model, Types, J, K, M, Jp, Jn, psi, Prob_of_claims, c, d, T)
    
    #g-definition
    Constraint.Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, Obs_claims, Lp, Ln, pi, c, op, on, g)
    
    #o-definition
    Constraint.Add_PremiumChangeDefinition(model,Types, K, L, L_var, epsilon, psi, op, on, c, Op, On)
    
    #premium_rules
    Constraint.Add_PremiumConstraints(model, K, pi, Types, Obs_claims, epsilon_p, epsilon_n, Lp, Ln, Op, On)
    
    #Op, On - O connection
    Constraint.Add_O_OpOn_Connection(model, L, K, epsilon, L_var, O, Op, On)
                
       
    return model


class Constraint:
    def Add_AbsoluteVariableDefinition(model, Types, K, Exp_claims, Obs_claims, Lp, Ln, pi, c, op, on, g):
        """ Constraint to define the g-variable when the premium may change """
        for i in Types:
            #g eltérés  
            for k in range(K+1):
                model += (Obs_claims[i]*c[k][i] + pulp.lpSum(op[k][l][i] for l in range(Lp)) - pulp.lpSum(on[k][l][i] for l in range(Ln))
                            +g[k][i]
                                    >= Exp_claims[i]*c[k][i], "c14_g_elteres_p_k"+str(k)+"_i"+str(i))
                model += (Obs_claims[i]*c[k][i] +  pulp.lpSum(op[k][l][i] for l in range(Lp)) - pulp.lpSum(on[k][l][i] for l in range(Ln))
                            -g[k][i]
                                    <= Exp_claims[i]*c[k][i], "c14b_g_elteres_n_k"+str(k)+"_i"+str(i))

    def Add_PremiumChangeDefinition(model,Types, K, L, L_var, epsilon, psi, op, on, c, Op, On):
        """ define the premium change variable """

        for i in Types:
            for k in range(K+1):
                for l in range(L):
                    if epsilon[l] > 0:
                        model += op[k][L_var[l]][i] >= epsilon[l]*(c[k][i] - psi[i]*(1-Op[k][L_var[l]])), "c17a_op_also_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                        model += op[k][L_var[l]][i] <= epsilon[l]*c[k][i] , "c17b_op_felso_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                        model += op[k][L_var[l]][i] <= epsilon[l]*psi[i]*Op[k][L_var[l]], "c17c_op_bin_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                    else:
                        model += on[k][L_var[l]][i] >= -epsilon[l]*(c[k][i] - psi[i]*(1-On[k][L_var[l]])), "c17a_on_also_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                        model += on[k][L_var[l]][i] <= -epsilon[l]*c[k][i] , "c17b_on_felso_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                        model += on[k][L_var[l]][i] <= -epsilon[l]*psi[i]*On[k][L_var[l]], "c17c_on_bin_k"+str(k)+"_l"+str(l) +"_i"+str(i)
                
                    
    def Add_PremiumConstraints(model, K, pi, Types, Obs_claims, epsilon_p, epsilon_n, Lp, Ln, Op, On):
        """ Constraint on the optimal premiums: """
        for k in range(K+1):
            #Egy osztalyban csak egy tipus dija lehet
            model+= pulp.lpSum(Op[k][l] for l in range(Lp)) + pulp.lpSum(On[k][l] for l in range(Ln)) <= 1, "c18_egyvalt"+str(k)
            for i in Types:
                #valtoztatott dij ne legyen negativ
                model += (Obs_claims[i]  + pulp.lpSum(epsilon_p[l]*Op[k][l] for l in range(Lp)) + pulp.lpSum(epsilon_n[l]*On[k][l] for l in range(Ln)) 
                      >= 0, "c15_dijpoz_k"+str(k)+"_i"+str(i))
            
            
        #alacsonyabb osztaly dija legyen kisebb
        for k in range(K):
            model += ( pulp.lpSum(epsilon_p[l]*Op[k][l] for l in range(Lp)) + pulp.lpSum(epsilon_n[l]*On[k][l] for l in range(Ln)) 
                      >= pulp.lpSum(epsilon_p[l]*Op[k+1][l] for l in range(Lp)) + pulp.lpSum(epsilon_n[l]*On[k+1][l] for l in range(Ln))  
                         , "c16_dijmon_k"+str(k))         
            
       
    def Add_O_OpOn_Connection(model, L, K, epsilon, L_var, O, Op, On):
        """ Connects the O and with the Op and On variables. """
        for l in range(L):
            for k in range(K+1):
                if epsilon[l] > 0:
                    model += O[k][l] == Op[k][L_var[l]], "c_20_O_Op"+str(k)+"_"+str(L_var[l])
                else:
                    model += O[k][l] == On[k][L_var[l]],  "c_20_O_On"+str(k)+"_"+str(L_var[l])
            