#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:09:02 2024

@author: ayselerkilet
"""
import gurobipy as gp
from gurobipy import GRB

c = {}  # Objective coefficients
a = {}  # Constraint coefficients
b = 0   # Constraint RHS

n = int(input(f'Enter n: '))

# input parameters
for i in range(1, n+1):
    c[i] = int(input(f'Enter objective coefficient for X{i}: '))

for i in range(1, n+1):
    a[i] = int(input(f'Enter constraint coefficient for X{i}: '))

b = int(input('Enter a constraint RHS (b value): '))

# Relaxation model 
m = gp.Model()

# relaxation variables
X = {i: m.addVar(vtype=GRB.CONTINUOUS, lb = 0, ub = 1, name=f'X{i}') for i in range (1, n+1)}

# objective function
m.setObjective(gp.quicksum(c[i] * X[i] for i in range (1, n+1)), GRB.MAXIMIZE)

# constraint
m.addConstr(gp.quicksum(a[i] * X[i] for i in range (1, n+1)) <= b, name='Constraint1')

#solving the LP relaxation
m.optimize()

cover_inequalities = [] #list for displaying cover inequalities

while True:
    L = []
    for i in range(1, n + 1):
        if 1 > X[i].x > 0:  # solution vector is not integer feasible
            L.append(i)
    if L:
        # add cover inequality
        m.addConstr(gp.quicksum(X[j] for j in L) <= len(L) - 1, name=f'Cover_{L}')
        
    if not L:
        break
    
    # cover inequality string
    inequality_str = ' + '.join(f'X{j}' for j in L) + f' <= {len(L) - 1}'
    
    # Store the inequality
    cover_inequalities.append(inequality_str)

    # Re-optimize the model
    m.optimize()

#print the nonzero solutions found
m.printAttr('X')
print(f'Optimum Vector X* : {m.X}')
print(f'Optimum Value (Z*): {m.objVal}')
print(f'Total number of cover inequalities added: {len(cover_inequalities)}')
# Display all cover inequalities
print('\nAll cover inequalities:')
for inequality in cover_inequalities:
    print(inequality)