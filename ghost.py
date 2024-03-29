import numpy as np
from utils import getShortestPath, getChoicesGhost

'''
Algorithms for ghost movement
'''

'''
Determines the next position for the ghost to move to, using a closest direction approach.
1. A: Adjacency list containing all of the vertices of the map and their neighbors.
2. v_pac: current (x,y) position of pacman
3. v_ghost: current (x,y) position of the ghost
4. d_ghost: current direction that the ghost is facing 
'''
def ghostMovement_1(A, v_pac, v_ghost, d_ghost):
    choices = getChoicesGhost(A, v_ghost, d_ghost)
    maxCos = -1
    if len(choices) == 1:
        return choices[0]
    for v in choices:
        v_rel = np.array(v_pac) - np.array(v_ghost)
        d = np.array(v) - np.array(v_ghost)
        cos = np.dot(d, v_rel) / (np.linalg.norm(d) * np.linalg.norm(v_rel))
        if cos > maxCos:
            maxCos = cos
            v_ghost = v
    return v_ghost


'''
Determines the next position for the ghost to move to using a shortest path approach.
1. A: Adjacency list containing all of the vertices of the map and their neighbors.
2. v_pac: current (x,y) position of pacman
3. v_ghost: current (x,y) position of the ghost
4. d_ghost: current direction that the ghost is facing 
'''
def ghostMovement_2(A, v_pac, v_ghost, d_ghost):
    choices = getChoicesGhost(A, v_ghost, d_ghost)
    if len(choices) == 1:
        return choices[0]
    V = list(A.keys())
    path = getShortestPath(V, A, v_pac, v_ghost, d_ghost)
    if len(path) == 1:
        return v_pac
    v_ghost = path[1]
    # breakpoint()
    return v_ghost