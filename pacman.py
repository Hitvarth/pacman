'''
Algorithms for pacman movement
'''
import numpy as np
from utils import getChoicesPacman, getNearestPelletDist
from board import symbols

def pacmanMovement_1(Map, A, v_pac, v_ghost, args):
    lam_p, lam_g = args.lam_p, args.lam_g
    C = getChoicesPacman(A, v_pac)
    max_score = -float('inf')
    for v in C:
        d_ghost = np.linalg.norm(np.array(v)-np.array(v_ghost))
        if d_ghost<2:
            continue
        score = lam_g*d_ghost
        if Map[v[0]][v[1]]==symbols["pellet"]:
            score += lam_p
        if score > max_score:
            max_score = score
            print(lam_g*d_ghost, lam_p)
            v_pac_new = v
    return v_pac_new

def pacmanMovement_3(Map, A, v_pac, v_ghost, args):
    lam_p, lam_g, lam_n = args.lam_p, args.lam_g, args.lam_n
    C = getChoicesPacman(A, v_pac)
    max_score = -float('inf')
    for v in C:
        d_ghost = np.linalg.norm(np.array(v)-np.array(v_ghost))
        d_pellet = getNearestPelletDist(Map, A, v)
        print(d_pellet)
        score = lam_g*d_ghost - lam_n*d_pellet
        if d_ghost<2:
            continue
        if Map[v[0]][v[1]]==symbols["pellet"]:
            score += lam_p
        if score > max_score:
            max_score = score
            print(lam_g*d_ghost, lam_n*d_pellet, lam_p)
            v_pac_new = v
    return v_pac_new


