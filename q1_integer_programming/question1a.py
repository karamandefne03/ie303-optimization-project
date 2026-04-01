# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:06:42 2024

@author: Defne Karaman
"""

import gurobipy as gp
from gurobipy import GRB

#create model instance
m = gp.Model()

#add the parameters
CH = 500 #hiring cost
CF = 1000 # firing cost
CI = 0.04 #inventory cost
K = 30000 #number ıf products produced by one worker in a year
I0 = 20000 #initial inventory
W0 = 3 #initial workforce
Dt = {1: 15, 2: 20, 3: 25, 4: 10, 5: 30} #demand forecast
CW = 25000 #worker salary for a year



#add the variables
T = 5  # Number of periods
It = {t: m.addVar(vtype=GRB.INTEGER, name=f"It_{t}") for t in range(1, T+1)}
Pt = {t: m.addVar(vtype=GRB.INTEGER, name=f"Pt_{t}") for t in range(1, T+1)}
Wt = {t: m.addVar(vtype=GRB.INTEGER, name=f"Wt_{t}") for t in range(1, T+1)}
Ht = {t: m.addVar(vtype=GRB.INTEGER, name=f"Ht_{t}") for t in range(1, T+1)}
Ft = {t: m.addVar(vtype=GRB.INTEGER, name=f"Ft_{t}") for t in range(1, T+1)}


#write the objective function
m.setObjective(CH * Ht + CF * Ft + CI * It + CW * Wt ,GRB.MINIMIZE)

#add the constraint
I0 = 20000  # Example initial inventory

# Add constraints for all periods for constraint 1
for t in range(1, T+1):
    if t == 1:
        # First period: reference initial inventory
        m.addConstr(It[t] == I0 + Pt[t] - Dt[t], name=f"c1_t{t}")
    else:
        # Subsequent periods: reference t-1 variables
        m.addConstr(It[t] == It[t-1] + Pt[t] - Dt[t], name=f"c1_t{t}")

c2 = m.addConstr(Pt = K * Wt)

# Add constraints for all periods for constraint 1
for t in range(1, T+1):
    if t == 1:
        # First period: reference initial inventory
        m.addConstr(Wt[t] == W0 + Ht[t] - Ft[t], name=f"c3_t{t}")
    else:
        # Subsequent periods: reference t-1 variables
        m.addConstr(Wt[t] == Wt[t-1] + Ht[t] - Ft[t], name=f"c1_t{t}")

#solving the model
m.optimize()

#print the nonzero solutions found
m.printAttr("X")









