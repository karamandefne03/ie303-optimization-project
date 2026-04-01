#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:33:15 2024

@author: ayselerkilet
"""

import gurobipy as gp
from gurobipy import GRB

# Initialize dictionaries
c = {}  # Objective coefficients
a = {}  # Constraint coefficients
b = 0   # Constraint RHS

n = int(input(f"Enter n: "))

# parameters
for i in range(1, n+1):
    c[i] = int(input(f"Enter objective coefficient for X{i}: "))  #objective coefficients

for i in range(1, n+1):
    a[i] = int(input(f"Enter constraint coefficient for X{i}: "))  #constraint coefficients

b = int(input("Enter a constraint RHS (b value): "))  # Read constraint RHS

#model 
m = gp.Model()

# binary variables
X = {i: m.addVar(vtype=GRB.BINARY, name=f"X{i}") for i in range (1, n+1)}

# objective function
m.setObjective(gp.quicksum(c[i] * X[i] for i in range (1, n+1)), GRB.MAXIMIZE)

# constraint
m.addConstr(gp.quicksum(a[i] * X[i] for i in range (1, n+1)) <= b, name="Constraint1")

# Solve the model
m.optimize()

#print the nonzero solutions found
m.printAttr("X")