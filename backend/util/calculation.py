# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:48:19 2020

@author: gyetm
"""
from scipy.stats import poisson
#import numpy as np
    


class distribution:
    #def __init__(self):
        
    def Binary(Exp_claims):
        """calcuate the binary probability distribution"""  
        prob_of_claims = {}
        for i in Exp_claims:
            prob_of_claims[i, 0] = 1- Exp_claims[i]        
            prob_of_claims[i, 1] = Exp_claims[i]
            
        return prob_of_claims
        
    def Poisson(Exp_claims, max_nbr_of_claims):
        """calculate the Poisson distribution, with top-sum """
        
        prob_of_claims = {}
        
        #I = len(Lambda)
        #lambda_m = np.empty([I,max_nbr_of_claims+1])
        #lamb_seged= np.empty([I,M])
        for i in Exp_claims:
            for m in range(max_nbr_of_claims):
                prob_of_claims[i,m] = poisson.pmf(m, Exp_claims[i])
                #sum_prob_temp[i,m] = prob_of_claims[i,m]
            prob_of_claims[i,max_nbr_of_claims] = 1 - sum(prob_of_claims[i,m] for m in range(max_nbr_of_claims))
    
        return prob_of_claims
    
    ##binomial
    
    
    
class solution:
    def optimal_premiums(model, Epsilon, nbr_of_classes):
        if model.status == 1:
            Pi_opt = {k: round(model._pi[k]+ sum(Epsilon[l]*model._O[k][l].varValue for l in range(len(Epsilon))), 3)
                    for k in range(nbr_of_classes)}
        else:
            Pi_opt = {k: round(model._pi[k],3) for k in range(nbr_of_classes)}
        return Pi_opt

    def optimal_TR(model, ruletype):
        
        if ruletype == "S":
            TR = {}
            for m in range(model._M+1):
                for j in model._J:
                    if model._T[j][m].varValue > 0:
                        TR[m] = j
        else:
            TR = {k: [] for k in range(model._K+1)}
            
            
            for k in TR:
                rule_k = {m: j for m in range(model._M+1) for j in model._J[k] if model._T[j,m,k].varValue > 0}
                TR[k] = rule_k
                            
        return TR
    
    def objective_value(stationary_probabilities,Premiums, Ratio_of_types, Exp_claims, round_value):
        """ calculate the rounded - objective value """
        Obj = sum(abs(round(Premiums[k], round_value) -Exp_claims[i])*Ratio_of_types[i]*stationary_probabilities[k,i] for k in Premiums for i in Ratio_of_types)
        return Obj
        
        
        
        
   
    def optimal_premium_variables(model, nbr_of_classes):
        Premiums = {}
        for k in range(nbr_of_classes):
            Premiums[k] = model._pi[k].varValue
        return Premiums
    
    def OP_group(stat_variables, premiums, Types, Exp_claims, Ratio_of_types, data):
        OP = {}
       
        for i in Types:
            if  "observable" not in data or data["observable"] == "False":
                Obs_part = 0
            else:
                Obs_part = data['Obs_claims'][i]
                
            OP[i] = sum(stat_variables[k,i] * (premiums[k]+ Obs_part) for k in premiums)/(Exp_claims[i]*Ratio_of_types[i])-1

        
        return OP
    
    def total_OP(stat_variables, premiums, Types, Exp_claims, Ratio_of_types, data, print_pay = True):
        TOP = {'AOP': 0, 'QOP': 0}
        for i in Types:
            if  "observable" not in data or data["observable"] == "False":
                Obs_part = 0
            else:
                Obs_part = data['Obs_claims'][i]
            
            
            TOP['AOP']+= abs(sum(stat_variables[k,i] * (premiums[k]+Obs_part) for k in premiums)-(Exp_claims[i]*Ratio_of_types[i]))
            if print_pay:
                print("     ", i, "---Pi", sum(stat_variables[k,i] * (premiums[k]+Obs_part) for k in premiums), "---Lam", Exp_claims[i]*Ratio_of_types[i])
            TOP['QOP']+= ((sum(stat_variables[k,i] * (premiums[k]+Obs_part) for k in premiums)-(Exp_claims[i]*Ratio_of_types[i]))**2)
           
        TOP['QOP'] = (TOP['QOP'])**(1/2)
              
        
        return TOP
    
    
    def convert_c_statvar(model, Types, nbr_of_classes, periods=0):
        stat_var= {}
        for i in Types:
            for k in range(nbr_of_classes):
                if periods == 0:
                    stat_var[k,i] =model._c[k][i].varValue
                else:
                    stat_var[k,i] =model._c[k][i][periods].varValue
                
        return stat_var
    ##OP
    ##profit-multiperiod


class premium:
    def proportional_scale(nbr_of_classes, Ratio_of_types, Exp_claims):
        """ Return the prpoprional premium scale """
        Max_Cummulative_ratio, Min_Cummulative_ratio = {}, {}
        
        Sorted_types = sorted(Exp_claims, key=Exp_claims.get, reverse=True)
        
        All_ratio = sum(Ratio_of_types.values())
        Total = 0
        

        for i in Sorted_types:
            Min_Cummulative_ratio[i] = round(Total, 9)
            Total += Ratio_of_types[i]/All_ratio
            Max_Cummulative_ratio[i] = round(Total, 9)
      
        Premiums = {k: Exp_claims[i] for k in range(nbr_of_classes+1) for i in Exp_claims 
                        if (k+1)/nbr_of_classes <= Max_Cummulative_ratio[i] and (k+1)/nbr_of_classes > Min_Cummulative_ratio[i]}
        
        return Premiums
        
        
        
    def linear_scale(nbr_of_classes, Exp_claims):
        """ Returns the linear premium scale """
        
        
        Premiums = {k: round(Exp_claims[max(Exp_claims, key=Exp_claims.get)] 
                    - k/(nbr_of_classes-1) *(Exp_claims[max(Exp_claims, key=Exp_claims.get)]- Exp_claims[min(Exp_claims, key=Exp_claims.get)]), 5)
                    for k in range(nbr_of_classes)}
        
        return Premiums        

        
    def min_almost(nbr_of_classes, Exp_claims):
        """ Returns the min lambda in almost each class, except the class0, in which the premium is the max lambda """
        
                
        Premiums = {k: min(Exp_claims.values()) for k in range(nbr_of_classes)}
        Premiums[0] =  max(Exp_claims.values())
       
        return Premiums        

    def max_almost(nbr_of_classes, Exp_claims):
        """ Returns the min lambda in almost each class, except the class0, in which the premium is the max lambda """
        
                
        Premiums = {k: max(Exp_claims.values()) for k in range(nbr_of_classes)}
        Premiums[nbr_of_classes-1] =  min(Exp_claims.values())
       
        return Premiums     
        
        
