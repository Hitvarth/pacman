from ghost import getChoicesGhost

def getChoicesPacman(A, v_pac):
    C = []
    for v in A[v_pac]:
        C.append(v)
    return C

def getShortestPath(V, A, v_pac, v_ghost, d_ghost):
    prev = {}
    for v in V:
        prev[v] = None
    choices = getChoicesGhost(A, v_ghost, d_ghost)
    for v in choices:
        prev[v] = v_ghost
    queue = []
    while len(queue) > 0:
        v_i = queue.pop()
        for v_j in A[v_i]:
            if prev[v_j] == None:
                prev[v_j] = v_i
                if v_j == v_pac:
                    break
                queue.append(v_j)
    path = [v_pac]
    v_curr = v_pac
    while v_curr is not None:
        v_curr = prev[v_curr]
        path.append(v_curr)
    path.reverse()
    return path


def getNearestPelletDist(Map, A, v):
    queue = []
    visited = []
    queue.append((v,0))
    while len(queue)>0:
        x,d = queue.pop()
        if Map[x[0]][x[1]] == True:     # the vertex has a pellet
            return d
        for n in A[x]:
            if n not in visited:
                queue.add((n, d+1))
                visited.add(n)
    return -1   # pellet not found, board completed