# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:36:47 2024

@author: Defne Karaman
"""

import gurobipy as gp
from gurobipy import GRB

#create model instance
m = gp.Model()

#add the variables
X1 = m.addVar(vtype = GRB.CONTINUOUS, name = "X1")
X2 = m.addVar(vtype = GRB.CONTINUOUS, name = "X2")

#write the objective function
m.setObjective(15 * X1 + 10 * X2, GRB.MINIMIZE)

#add the constraint
c1 = m.addConstr(4 * X1 + X2 >= 6)
c2 = m.addConstr(X1 + 2 * X2 >= 3)
c3 = m.addConstr(X1 + X2 >= 3)

#solving the model
m.optimize()

#print the nonzero solutions found
m.printAttr("X")