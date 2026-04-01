# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:42:52 2024

@author: Defne Karaman
"""

import time
import matplotlib.pyplot as plt
from gurobipy import Model, GRB, quicksum

def solve_magic_square(n):
    # Record start time
    start_time = time.time()

    magic_constant = n * (n**2 + 1) // 2
    numbers = range(1, n**2 + 1)

    # Create the model
    model = Model("Magic_Square")
    model.setParam("OutputFlag", 0)  # Suppress Gurobi output

    # Decision variables
    z = model.addVars(n, n, numbers, vtype=GRB.BINARY, name="z")
    x = model.addVars(n, n, vtype=GRB.INTEGER, name="x")

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

    # Set a time limit (optional for larger grids)
    model.setParam("TimeLimit", 3600)

    # Optimize the model
    model.optimize()

    # Record end time
    end_time = time.time()

    # Calculate runtime
    runtime = end_time - start_time

    # Retrieve solution if feasible
    if model.status == GRB.OPTIMAL or model.status == GRB.TIME_LIMIT:
        magic_square = [[int(x[i, j].x) for j in range(n)] for i in range(n)]
    else:
        magic_square = None

    return runtime, magic_square

def print_square(square):
    """Helper function to print a magic square in a formatted grid."""
    if square:
        size = len(square)
        max_val = max(max(row) for row in square)
        cell_width = len(str(max_val)) + 2  # Adjust cell width for alignment
        for row in square:
            print("".join(f"{cell:{cell_width}}" for cell in row))
    else:
        print("No solution found.")

# Solve for grid sizes 3x3 to 10x10 and record runtimes and squares
grid_sizes = range(3, 11)
runtimes = []
magic_squares = {}

for size in grid_sizes:
    print(f"\nSolving for {size}x{size} magic square...")
    runtime, square = solve_magic_square(size)
    runtimes.append(runtime)
    magic_squares[size] = square
    print(f"Runtime for {size}x{size}: {runtime:.2f} seconds")
    print(f"Magic Square for {size}x{size}:")
    print_square(square)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(grid_sizes, runtimes, marker="o", linestyle="-", color="b")
plt.title("Runtime vs Grid Size for Magic Square Model")
plt.xlabel("Grid Size (n x n)")
plt.ylabel("Runtime (seconds)")
plt.grid(True)
plt.xticks(grid_sizes)
plt.show()

