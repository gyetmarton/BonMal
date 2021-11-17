# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:18:04 2020

@author: gyetm
"""
import util.calculation as calculation

def environment_print(model, ruletype, time = None, Obj = None, TR = None, premiums = None):
    print(">> >> >> XXX SOLUTION XXX << << <<")
    if time is not None:
        print_time(model)
    if Obj is not None:
        print_objective(model)
    
    if TR is not None:
        if ruletype == "S":
            print_transition_rule(model)
        else:
            print_multi_transition_rule(model)
            
    
    if premiums is not None:
        print(">> Optimal Premiums:")
        print("~~", premiums)
       

def print_time(model):
    print("~~~ solution time: ", model.solutionTime ,"sec")

def print_objective(model):
    print("~~~ objective value: ", model.objective.value() )

def print_transition_rule(model):
    print(">> Transition rules: ")
    for m in range(model._M+1):
        for j in model._J:
            if round(model._T[j][m].varValue,0) > 0:
                print("       ",m, "claim: ", j )
                
def print_multi_transition_rule(model):
    print(">> Transition rules: ")
    for m in range(model._M+1):
        for k in range(model._K+1):
            for j in model._J[k]:
                if model._T[j,m,k].varValue > 0:
                    print("class", k, "with",m, "claim: ", j )
      
         

def print_status(status):
    print(" ¤¤","\n")
    if status== -1:
        print("Model is infeasible")
    elif status == -2:
        print("Model is unbounded")
    else:
        print("Other mistake,...")
    print("\n","¤¤")
    
def print_statprob_var(model, Types, nbr_of_classes):
     for i in Types:
        print(">>>> ", i, " <<<<")
        for k in range(nbr_of_classes):
           print(k, " ", model._c[k][i].varValue)
    
    
    
    
    
"""
print("########################################","\n")
print(model.solutionTime)
print( model.objective.value())
#print("Solution found in ",model.solutionTime, "sec" )
#print("Obj.value: ", model.objective.value())
print("Transition rule: ")


for k in range(K+1):
    print(round(pi[k]-2**(L+1)*epsilon* On[k].varValue + sum(2**(l)*epsilon*O[k][l].varValue for l in range(L+1)), 5))


for i in range(I):
    for k in range(K+1):
        #print("c", k ,"_", i ,  " = ", c[k][i].varValue)
        print(c[k][i].varValue)
        
"""