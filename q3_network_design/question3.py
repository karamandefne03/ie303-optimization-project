# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:45:35 2024

@author: Defne Karaman
"""

import matplotlib.pyplot as plt
import networkx as nx
from gurobipy import Model, GRB, quicksum

# Number of agents (nodes)
n = 7

# Create the model for one-way channels
model = Model("One_Way_Channels")

# Variables: x[i,j] = 1 if there is a directed edge from agent i to agent j
x = model.addVars(n, n, vtype=GRB.BINARY, name="x")

# Objective: Minimize the total number of directed edges
model.setObjective(quicksum(x[i, j] for i in range(n) for j in range(n) if i != j), GRB.MINIMIZE)

# Constraints: each agent must have exactly one outgoing and one incoming edge
for i in range(n):
    model.addConstr(quicksum(x[i, j] for j in range(n) if i != j) == 1, f"outgoing_{i}")
    model.addConstr(quicksum(x[j, i] for j in range(n) if i != j) == 1, f"incoming_{i}")

# Relaxed connectivity constraint: Ensure the network is strongly connected
for i in range(n):
    for j in range(n):
        if i != j:
            model.addConstr(quicksum(x[i, k] for k in range(n) if k != i) >= 1, f"relaxed_connect_{i}_{j}")

# Optimize the model
model.optimize()

# Function to print the two-way communication network (undirected)
def print_two_way_network():
    print("\nTwo-Way Channel Network (Undirected):")
    for i in range(n):
        for j in range(i+1, n):  # Print only once for each pair (i, j)
            print(f"Agent {i+1} <-> Agent {j+1}")

# Function to print the one-way communication network (directed)
def print_one_way_network():
    print("\nOne-Way Channel Network (Directed):")
    for i in range(n):
        for j in range(n):
            if i != j and x[i, j].x > 0.5:  
                print(f"Agent {i+1} -> Agent {j+1}")

# Function to plot the two-way communication network
def plot_two_way_network():
    G = nx.Graph()  # Undirected graph for two-way communication
    for i in range(n):
        for j in range(i+1, n):  # Add edges for two-way communication
            G.add_edge(i+1, j+1)
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_size=700, node_color="lightblue", font_size=15, font_weight="bold", edge_color="gray")
    plt.title("Two-Way Communication Network (Undirected)")
    plt.show()

# Function to plot the one-way communication network
def plot_one_way_network():
    G = nx.DiGraph()  # Directed graph for one-way communication
    for i in range(n):
        for j in range(n):
            if i != j and x[i, j].x > 0.5:  
                G.add_edge(i+1, j+1)  
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_size=700, node_color="lightgreen", font_size=15, font_weight="bold", edge_color="gray", arrowsize=20)
    plt.title("One-Way Communication Network (Directed)")
    plt.show()

# Output the results
if model.status == GRB.OPTIMAL:
    print_two_way_network()  
    print_one_way_network()  
    plot_two_way_network()  
    plot_one_way_network()  
else:
    print("No optimal solution found.")
