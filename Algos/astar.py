# trying to learn/implement the A* algorithm

"""
F = G + H
F, G, and H are variables in each node of our adj_list
  F = function of total cost
  G = distance between current node and start node
  H = heuristic - estimated cost/distance from current node to end node
                - a function that uses some best guess
                - always underestimates value
                - many different heuristic functions

Heuristic functions:
  - straight line heuristic: calculates euclidean distance between two nodes
  - landmark heuristic: preselect important nodes from graph; use djiksta from set

right choice heavily depends on model
"""

"""
Steps

1. add start node to queue
2. repeat the following
  - look for lowest total cost; F
  - select node and add to closed list; set to mark as seen
  - check all 8 adjacent squares
    - if not valid move or already seen ignore
    - otherwise calculate f, g, and heuristic function
    

"""