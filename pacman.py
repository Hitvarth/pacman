'''
Algorithms for pacman movement
'''
import numpy as np
from utils import getChoicesPacman, getNearestPelletDist
from board import symbols

def pacmanMovement_1(Map, A, v_pac, v_ghost, lam_p, lam_g):
    C = getChoicesPacman(A, v_pac)
    max_score = -float.inf
    for v in C:
        d_ghost = np.linalg.norm(np.array(v)-np.array(v_ghost))
        score = lam_g*d_ghost
        if Map[v[0]][v[1]]==symbols["pellet"]:
            score += lam_p
        if score > max_score:
            max_score = score
            v_pac_new = v
    return v_pac_new

def pacmanMovement_3(Map, A, v_pac, v_ghost, lam_p, lam_g, lam_n):
    C = getChoicesPacman(A, v_pac)
    max_score = -float.inf
    for v in C:
        d_ghost = np.linalg.norm(np.array(v)-np.array(v_ghost))
        d_pellet = getNearestPelletDist(Map, A, v)
        score = lam_g*d_ghost - lam_n*d_pellet
        if Map[v[0]][v[1]]==symbols["pellet"]:
            score += lam_p        
        if score > max_score:
            max_score = score
            v_pac_new = v
    return v_pac_new


