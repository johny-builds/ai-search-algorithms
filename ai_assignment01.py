'''
Johnathon Rodriguez
jr1202
AI Assignment 01

**Question 3**
Trace the operation of A* search applied to the problem of getting to Bucharest
from Lugoj
using the straight-line distance heuristic.
That is, show the sequence of nodes that the algorithm will consider and the f, g,
and h scores for each node (20 points).
'''

from collections import deque
from pprint import pprint
from typing import Any
from anytree import Node, RenderTree, AsciiStyle, ContStyle, PreOrderIter
from anytree import search

# choose the starting city
start = "lugoj"

# first bring in the data for the different functions of A*.
# I need the heuristics (straight line data) and the actual cost for each parent to
# child relationship which will be stored in node data

### HEURISTICS ##
strght_line_distance_2_bucharest = {
    "arad": 366,
    "bucharest": 0,
    "craiova": 160,
    "dobreta": 242,
    "eforie": 161,
    "fagaras": 178,
    "giurgiu": 77,
    "hirsova": 151,
    "lasi": 226,
    "lugoj": 244,
    "mehadia": 241,
    "neamt": 234,
    "oradea": 380,
    "pitesti": 98,
    "rimnicu vilcea": 193,
    "sibiu": 253,
    "timisoara": 329,
    "urziceni": 80,
    "vaslui": 199,
    "zerind": 374
}

## DICTIONARY OF CITIES ##
# displays distance to children in tuple first item
# list of children, each child is a tuple [0] = name of city [1] = distance to child
dictionary_of_cities = {
    "arad": [
        ("zerind", 75),
        ("sibiu", 140),
        ("timisoara", 118)
    ],
    "bucharest": [
        ("giurgiu", 90),
        ("pitesti", 101),
        ("fagaras", 211),
        ("urziceni", 85)
    ],
    "craiova": [
        ("dobreta", 120),
        ("rimnicu vilcea", 146),
        ("pitesti", 138)
    ],
    "dobreta": [
        ("craiova", 120),
        ("mehadia", 75)
    ],
    "eforie": [
        ("hirsova", 86)
    ],
    "fagaras": [
        ("sibiu", 99),
        ("bucharest", 211)
    ],
    "giurgiu": [
        ("bucharest", 90)
    ],
    "hirsova": [
        ("urziceni", 98),
        ("eforie", 86)
    ],
    "lasi": [
        ("neamt", 87),
        ("vaslui", 92)
    ],
    "lugoj": [
        ("mehadia", 70),
        ("timisoara", 111)
    ],
    "mehadia": [
        ("lugoj", 70),
        ("dobreta", 75)
    ],
    "neamt": [
        ("lasi", 87)
    ],
    "oradea": [
        ("zerind", 71),
        ("sibiu", 151)
    ],
    "pitesti": [
        ("rimnicu vilcea", 97),
        ("craiova", 138),
        ("bucharest", 101)
    ],
    "rimnicu vilcea": [
        ("sibiu", 80),
        ("craiova", 146),
        ("pitesti", 97)
    ],
    "sibiu": [
        ("rimnicu vilcea", 80),
        ("fagaras", 99),
        ("oradea", 151),
        ("arad", 140)
    ],
    "timisoara": [
        ("lugoj", 111),
        ("arad", 118)
    ],
    "urziceni": [
        ("bucharest", 85),
        ("vaslui", 142),
        ("hirsova", 98)
    ],
    "vaslui": [
        ("urziceni", 142),
        ("lasi", 92)
    ],
    "zerind": [
        ("oradea", 71),
        ("arad", 75)
    ]
}

# starting heuristic
heuristic = strght_line_distance_2_bucharest[start]
children = dictionary_of_cities[start]

# create start node
root = Node(start,
            g=0,
            f=strght_line_distance_2_bucharest[start],
            h=strght_line_distance_2_bucharest[start])

priority_queue = [(root, children)]
closed = set()
best_g = {start: 0}
step = 0

print("---PATH CHOSEN BY A* ALGO TO GET TO GOAL---")
while priority_queue:
    parent, children = min(priority_queue, key=lambda x: x[0].f)
    priority_queue.remove((parent, children))

    if parent.name in closed:
        continue
    closed.add(parent.name)

    step += 1
    parent.step = step
    print(f"Step {step}: {parent.name} (g={parent.g}, h={parent.h}, f={parent.f})")

    if parent.name == "bucharest":
        print("Goal reached!")
        goal_node = parent
        break

    for kid_name, cost in children:
        g_new = parent.g + cost
        h_new = strght_line_distance_2_bucharest[kid_name]
        f_new = g_new + h_new

        if kid_name not in best_g or g_new < best_g[kid_name]:
            best_g[kid_name] = g_new
            kid_node = Node(kid_name, parent=parent, g=g_new, h=h_new, f=f_new)
            if kid_name in dictionary_of_cities:
                priority_queue.append((kid_node, dictionary_of_cities[kid_name]))

print("\t\n--- Search Tree ---\nEntire tree structure with f,g,h values")
for pre, fill, node in RenderTree(root):
    print(f"\t{pre}{node.name} (g={node.g}, h={node.h}, f={node.f})")

'''
4: Implement DFS, BFS, and A* for the problem of getting to Bucharest from Arad.
You can use Python for the implementation.
Please present the path each algorithm will choose (45 points).
'''

print()
print("---------------------(QUESTION 4)--------------------------------\n")

# construct path from goal to root
path = []
node = goal_node
while node:
    path.append(node)
    node = node.parent
path_set = set(path)

print("\n--- A* Search Tree (whole tree) ---")
for pre, fill, node in RenderTree(root):
    step_str = f" [step {getattr(node, 'step', '-')}]"
    print(f"{pre}{node.name} (g={node.g}, h={node.h}, f={node.f}){step_str}")

print("\n--- Search Tree with A* (path only)---")
for pre, fill, node in RenderTree(root):
    if node in path_set:
        print(f"{pre}{node.name} (g={node.g}, h={node.h}, f={node.f})")
    else:
        " "

# ---BFS---
root = Node(start, g=0)
queue = deque([root])
visited = set([start])
goal_node = None
goal = "bucharest"  # Define the goal city
step = 0

while queue:
    parent = queue.popleft()
    step += 1
    parent.step = step

    # check for goal
    if parent.name == goal:
        goal_node = parent
        break

    # expand children
    for kid_name, cost in dictionary_of_cities.get(parent.name, []):
        if kid_name not in visited:
            visited.add(kid_name)
            kid_node = Node(kid_name, parent=parent, g=parent.g + cost)
            queue.append(kid_node)

# make the bfs path
path = []
if goal_node:
    cur = goal_node
    while cur:
        path.append(cur)
        cur = cur.parent
    path.reverse()

# show the whole tree, every node with its step
print("\n--- BFS Search Tree (whole tree) ---")
for pre, fill, node in RenderTree(root):
    step_str = f"[step {getattr(node, 'step', '-')}]"
    print(f"{pre}{node.name} (g={node.g}) {step_str}")

print("\n--- Search Tree with BFS (path only) ---")
path_set = set(path)
for pre, fill, node in RenderTree(root):
    if node in path_set:  # only show nodes on path
        step_str = f"[step {getattr(node, 'step', '-')}]"
        print(f"{pre}{node.name} (g={node.g}) {step_str}")

# ---DFS---
root = Node(start, g=0)
stack = [root]
visited = set([start])
goal_node = None
step = 0

while stack:
    parent = stack.pop()
    step += 1
    parent.step = step

    # check the goal
    if parent.name == goal:
        goal_node = parent
        break

    # expand children
    for kid_name, cost in dictionary_of_cities.get(parent.name, []):
        if kid_name not in visited:
            visited.add(kid_name)
            kid_node = Node(kid_name, parent=parent, g=parent.g + cost)
            stack.append(kid_node)

# make the dfs path
path = []
if goal_node:
    cur = goal_node
    while cur:
        path.append(cur)
        cur = cur.parent
    path.reverse()

# print the path only
print("\n--- DFS Search Tree (whole tree) ---")
for pre, fill, node in RenderTree(root):
    step_str = f" [step {getattr(node, 'step', '-')}]"
    print(f"{pre}{node.name} (g={node.g}){step_str}")

print("\n--- Search tree with DFS (path only) ---")
path_set = set(path)
for pre, fill, node in RenderTree(root):
    if node in path_set:
        step_str = f" [step {getattr(node, 'step', '-')}]"
        print(f"{pre}{node.name} (g={node.g}){step_str}")
