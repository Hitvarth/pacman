import numpy as np
from board import symbols

'''
Gets the possible next positions that the ghost can travel to.
1. A: Adjacency list containing all of the vertices of the map and their neighbors.
2. v_ghost: current (x,y) position of the ghost
3. d_ghost: current direction that the ghost is facing 
-> (can be (0,1), (0,-1), (1,0), and (-1,0) to represent right, left, up, and down)
'''
def getChoicesGhost(A, v_ghost, d_ghost):
    choices = []
    for v in A[v_ghost]:
        # Ghosts cannot perform 180s in their direction
        if all(np.array(v) - np.array(v_ghost) == -np.array(d_ghost)):
            continue
        choices = choices + [v]
    return choices


def getChoicesPacman(A, v_pac):
    C = []
    for v in A[v_pac]:
        C.append(v)
    return C

def getShortestPath(V, A, v_pac, v_ghost, d_ghost):
    prev = {}
    # initially, every vertices' prev is None
    for v in V:
        prev[v] = None
    # acquire all of the possible next vertices for the ghost
    choices = getChoicesGhost(A, v_ghost, d_ghost)
    queue = []
    # set the previous for all of the neighbors to the position of the ghost
    for v in choices:
        prev[v] = v_ghost
        queue.append(v)
    while len(queue) > 0:
        # print('queue: ', queue)
        v_i = queue.pop(0)
        for v_j in A[v_i]:
            if prev[v_j] == None:
                prev[v_j] = v_i
                if v_j == v_pac:
                    break
                queue.append(v_j)
    path = [v_pac]
    v_curr = v_pac
    # print(prev[v_ghost])
    while v_curr is not v_ghost:
        v_curr = prev[v_curr]
        path.append(v_curr)
    path.reverse()
    return path


def getNearestPelletDist(Map, A, v):
    queue = []
    visited = []
    queue.append((v,0))
    while len(queue)>0:
        x,d = queue.pop(0)
        if Map[x[0]][x[1]] == symbols['pellet']:     # the vertex has a pellet
            return d
        for n in A[x]:
            if n not in visited:
                queue.append((n, d+1))
                visited.append(n)
    return -1   # pellet not found, board completed