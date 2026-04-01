# IE303 Optimization Project – Gurobi Models

## Overview
This project was developed for the IE303 course (Modeling and Methods in Optimization) and focuses on solving various optimization problems using Gurobi in Python.

The project covers integer programming, LP relaxation, cutting planes, network design, and combinatorial optimization.

---

## Objectives
- Model real-world problems using integer programming
- Apply LP relaxation techniques
- Implement cutting plane methods (cover inequalities)
- Solve combinatorial optimization problems
- Analyze computational performance

---

## Topics Covered

### 1. Integer Programming & LP Relaxation
- Solved an integer program and its LP relaxation
- Applied Chvátal–Gomory cutting planes to improve solution quality

### 2. Knapsack Problem & Cutting Planes
- Implemented a binary knapsack problem
- Developed an algorithm to iteratively add cover inequalities
- Improved LP relaxation to reach integer optimal solution

### 3. Network Design Optimization
- Modeled a communication network problem
- Minimized number of one-way communication channels
- Ensured full connectivity between agents

### 4. Magic Square Optimization
- Formulated magic square as an integer programming problem
- Solved for sizes from 3×3 to 10×10
- Analyzed runtime complexity
- Visualized runtime growth

---

## Technologies Used
- Python
- Gurobi (gurobipy)
- Matplotlib (for visualization)
- NetworkX (for graph modeling)

---

## Project Structure
```
ie303-optimization-project/
├── report/
│   └── Report.pdf
├── q1_integer_programming/
├── q2_knapsack_cutting_planes/
├── q3_network_design/
├── q4_magic_square/
```

---

## How to Run
1. Install Gurobi and activate a license  
2. Install required libraries:
```bash
pip install gurobipy matplotlib networkx
```

3. Run any script:
```bash
python question3.py
```

---

## Note on Gurobi
This project uses Gurobi, which requires a valid license.  
Students can obtain a free academic license.

---

## Industrial Engineering Perspective
This project demonstrates:
- Optimization modeling
- Decision-making under constraints
- Resource allocation problems
- Algorithmic improvement (cutting planes)
- Computational complexity analysis

---

## 📌 Key Takeaway
This project highlights the use of advanced optimization techniques to solve structured decision problems efficiently using mathematical modeling.
