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

class Node:
  def __init__(self, parent=None, position=None):
    self.parent = parent # need to track previous node
    self.position = position

    self.g = 0 # distnace from current and src node
    self.h = 0 # heuristic function
    self.f = 0



# given matrix of 0s and 1s
# find path from src to target
# 1s represent walls and 0s represent an empty valid space/move
# start and end are x, y coordinates
def a_star(maze, start, end):

  # create start/end nodes
  src = Node(None, start)
  target = Node(None, end)

  q = deque()
  seen = set()

  while q:
    # extract node with smallest f value/cost from deque
    curr_node = q.popleft()
    for other_node in q:
      if other_node.f < curr_node.f:
        curr_node = other_node
      
    # add node to seen/visited list
    seen.add(curr_node)

    if curr_node == target:
      


    



  
