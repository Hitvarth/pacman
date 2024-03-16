import matplotlib.pyplot as plt
import time
import numpy as np

import sys 
sys.path.append("../pacman")

from board import getAdjacencyList
from pacman import pacmanMovement_1, pacmanMovement_3
# from ghost import ghostMovement_1, ghostMovement_2

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-n_max', type=int, help='Max number of rows', default=1000)

parser.add_argument('--lam_p', '-lp', type=float, help='Pellet importance weight', default=1)
parser.add_argument('--lam_g', '-lg', type=float, help='Ghost importance weight', default=1)
parser.add_argument('--lam_n', '-ln', type=float, help='Nearest pellet importance weight', default=1)

args = parser.parse_args()

def generateRandomMap(n, m, p):
    '''
    Generates a random map of size n x m with p probability of a cell being a wall.
    '''
    board = np.random.choice(['W', '.', ' '], size=(n, m), p=[p, 1-p, 0])
    return board

times_1, times_3 = [], []
for i in range(10, args.n_max):
    print('\r', i, end='')
    board = list(generateRandomMap(i, i, 0.1))
    board[i//2][i//2] = '.'
    board[i//4][i//4] = '.'
    A = getAdjacencyList(board)
    breakpoint()
    v_pac = (i//2, i//2)    #initial pacman position
    v_ghost = (i//4, i//4)  #initial ghost position
    # d_ghost = (0,1)     #initial ghost dir

    s = time.time()
    pacmanMovement_1(board, A, v_pac, v_ghost, args)
    times_1.append(time.time()-s)

    s = time.time()
    pacmanMovement_3(board, A, v_pac, v_ghost, args)
    times_3.append(time.time()-s)

plt.figure(figsize=(7,7), dpi=300)
plt.plot(np.arange(10, args.n_max), times_1, '-o', label='Pacman 1')
plt.plot(np.arange(10, args.n_max), times_3, '-o', label='Pacman 3')
plt.xlabel('Map size')
plt.ylabel('Time (s)')
plt.legend()
plt.savefig('time_algo.png')


# with open('results.txt', 'w') as f:
#     f.write('Pacman 1: ' + str(times_1) + '\n')
#     f.write('Pacman 3: ' + str(times_3) + '\n')







