'''
Code to run the game
'''

from board import board, adjacency_list, symbols
import argparse
import numpy as np
from time import sleep

from pacman import pacmanMovement_1, pacmanMovement_3
from ghost import ghostMovement_1, ghostMovement_2

parser = argparse.ArgumentParser(description='Run the pacman game')
parser.add_argument('--s_pac', '-sp', type=int, help='Pacman speed', default=1)
parser.add_argument('--s_ghost', '-sg', type=int, help='Ghost speed', default=1)
parser.add_argument('--lam_p', '-lp', type=float, help='Pellet importance weight', default=1)
parser.add_argument('--lam_g', '-lg', type=float, help='Ghost importance weight', default=1)
parser.add_argument('--lam_n', '-ln', type=float, help='Nearest pellet importance weight', default=1)
parser.add_argument('--algo_pac', '-ap', type=int, help='Algorithm to use for pacman', default=1, choices=[1, 3])
parser.add_argument('--algo_ghost', '-ag', type=int, help='Algorithm to use for ghost', default=1, choices=[1, 2])
args = parser.parse_args()

pacmanAlgos = {
    1: pacmanMovement_1,
    3: pacmanMovement_3
}
ghostAlgos = {
    1: ghostMovement_1,
    2: ghostMovement_2
}

pacmanMovement = pacmanAlgos[args.algo_pac]
ghostMovement = ghostAlgos[args.algo_ghost]

def runGame(s_pac, s_ghost):
    A = adjacency_list  
    v_pac = (22, 14)    #initial pacman position
    v_ghost = (10, 14)  #initial ghost position
    d_ghost = (0,1)     #initial ghost dir

    # importance weights for pellets, ghosts, nearest pellet
    lam_p, lam_g, lam_n = 1, 1, 1       ## need to tune these!!

    solution_path = [v_pac]
    
    tick = 0    # runtime clock

    num_pellets = 240 # initial num pellets
    pacman_alive = True

    div_pac, div_ghost = int(1/s_pac), int(1/s_ghost)

    # game loop
    while (num_pellets > 0 and pacman_alive):

        if (tick % div_pac == 0):
            v_pac = pacmanMovement(board, A, v_pac, v_ghost, args)  #<---------------
            solution_path.append(v_pac)
            #update board
            if board[v_pac[0]][v_pac[1]] == symbols["pellet"]:
                num_pellets -= 1
                board[v_pac[0]][v_pac[1]] = symbols["empty"]

        if (tick % div_ghost == 0):
            v_ghost_next = ghostMovement (A, v_pac, v_ghost, d_ghost) #<---------------
            d_ghost_np = np.array(v_ghost_next) - np.array(v_ghost)
            d_ghost = (d_ghost_np[0],d_ghost_np[1])
            v_ghost = v_ghost_next
            
        #check pacman alive
        if (v_pac == v_ghost):
            pacman_alive = False

        # display board
        line_num = 0
        print('\n###  clock: ' + str(tick))
        for line in board:
            # line_copy = copy.deepcopy(line)
            line_copy = line.copy()
            if (line_num == v_pac[0]):
                line_copy[v_pac[1]] = "P"
            if (line_num == v_ghost[0]):
                line_copy[v_ghost[1]] = "G"
            print(''.join(line_copy))
            line_num += 1

        #update clock
        tick += 1
        # breakpoint()
        if tick > 1000:
            breakpoint()
            break
        sleep(0.1)

    if (pacman_alive):
        return solution_path
    else:
        return []



# Complete the board based on the picture provided by the user, row by row.

# Complete the rest of the board by transcribing from the image row by row.

if __name__=="__main__":
    
    runGame(args.s_pac, args.s_ghost) 
    