# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:31:15 2024

@author: Defne Karaman
"""

import time
from gurobipy import Model, GRB, quicksum

# Start the timer
start_time = time.time()

# Parameters
n = 8
magic_constant = n * (n**2 + 1) // 2  # 260
numbers = range(1, n**2 + 1)  # All integers from 1 to n^2

# Create the model
model = Model("Magic_Square")

# Decision variables
z = model.addVars(n, n, numbers, vtype=GRB.BINARY, name="z")  # Binary assignment variables
x = model.addVars(n, n, vtype=GRB.INTEGER, name="x")  # Integer variables for the grid

# Link binary variables to the grid variables
model.addConstrs(
    (x[i, j] == quicksum(k * z[i, j, k] for k in numbers) for i in range(n) for j in range(n)),
    name="Linking"
)

# Ensure each integer appears exactly once in the grid
model.addConstrs(
    (quicksum(z[i, j, k] for i in range(n) for j in range(n)) == 1 for k in numbers),
    name="UniqueAssignment"
)

# Ensure each cell contains exactly one number
model.addConstrs(
    (quicksum(z[i, j, k] for k in numbers) == 1 for i in range(n) for j in range(n)),
    name="CellAssignment"
)

# Row sums must equal the magic constant
model.addConstrs(
    (quicksum(x[i, j] for j in range(n)) == magic_constant for i in range(n)),
    name="RowSums"
)

# Column sums must equal the magic constant
model.addConstrs(
    (quicksum(x[i, j] for i in range(n)) == magic_constant for j in range(n)),
    name="ColumnSums"
)

# Diagonal sums must equal the magic constant
model.addConstr(
    quicksum(x[i, i] for i in range(n)) == magic_constant,
    name="MainDiagonalSum"
)
model.addConstr(
    quicksum(x[i, n - i - 1] for i in range(n)) == magic_constant,
    name="AntiDiagonalSum"
)

# Set a time limit of 1 hour
model.setParam("TimeLimit", 3600)

# Optimize the model
model.optimize()

# Stop the timer
end_time = time.time()

# Calculate and display runtime
runtime = end_time - start_time
print(f"Total runtime: {runtime:.2f} seconds")

# Function to print the magic square in a formatted grid
def print_formatted_square(square):
    """Prints the magic square in a neatly formatted grid."""
    if square:
        max_val = max(max(row) for row in square)  # Largest number in the square
        cell_width = len(str(max_val)) + 2  # Width of each cell, for alignment
        for row in square:
            print("".join(f"{val:{cell_width}}" for val in row))
    else:
        print("No magic square found.")

# Output the results
if model.status == GRB.OPTIMAL or model.status == GRB.TIME_LIMIT:
    magic_square = [[int(x[i, j].x) for j in range(n)] for i in range(n)]
    print("\nMagic Square Found:")
    print_formatted_square(magic_square)
else:
    print("No solution found within the time limit.")

