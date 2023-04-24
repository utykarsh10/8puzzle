from __future__ import annotations
from board import Board
from collections.abc import Callable

import numpy as np
import heapq as hq

'''
Heuristics
'''
def MT(board: Board) -> int:
    #MISPLACED TILES
    #f = h + g
    #g can be the number of misplaced tiles 
    tiles = 0

    for i in range(3):
        for j in range(3):
            if(board.state[i][j] != board.solution[i][j] and board.state[i][j] != 0):
                tiles+=1

    return tiles

    

    return 

def CB(board: Board) -> int:
    #City Block Distance or Manhattan Distance 
    dist = 0

    for i in range(3):
        for j in range(3):
            if board.state[i,j] != 0:
                x, y = np.argwhere(board.solution == board.state[i,j])[0]
                dist += abs(i-x) + abs(j-y)

    return dist


def NA(board: Board) -> int:
    return 



'''
A* Search 
'''
def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    statelist = []
    movelist = []

    #bfs
    if(heuristic == 0):
        queue = [board]
        while queue:
            board = queue.pop(0)

            if(board.goal_test()):
                print(board)
                print("YAY")
                #print(movelist)
                break

            print(board.state)
            
            for state in board.next_action_states():
                if(state[0] not in statelist):
                    board = state[0]
                    queue.append(board)
                    statelist.append(state[0])
                    movelist.append(state[1])

    

    return board
