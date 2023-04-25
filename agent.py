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
    #Number of inversions
    flat_arr = board.state.flatten()
    flat_len = len(flat_arr)

    inversions = 0
    for i in range(flat_len):
        for j in range(i + 1, flat_len):
            if flat_arr[i] and flat_arr[j] and flat_arr[i] > flat_arr[j]:
                inversions += 1
    return inversions





'''
A* Search 
'''
def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    statelist = []
    movelist = []

    #bfs when heuristic = 0
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


    #With heuristic 
    else:
       
        moves_and_costs = {board: ([], 0)}

        queue = [(0, board)]
        hq.heapify(queue)

        while queue:
            #lowest f value state
            _, current_board = hq.heappop(queue)

            if current_board.goal_test() == True:
                #return current_board, moves_and_costs[current_board]
                return moves_and_costs[current_board][0]

            next_states = current_board.next_action_states()

            for next_board, move in next_states:
                g = moves_and_costs[current_board][1] + 1  
                h = heuristic(next_board)
                f = g + h

                if next_board not in moves_and_costs:
                    moves_and_costs[next_board] = (moves_and_costs[current_board][0] + [move], g)
                    hq.heappush(queue, (f, next_board))

                elif g < moves_and_costs[next_board][1]:
                    moves_and_costs[next_board] = (moves_and_costs[current_board][0] + [move], g)

        return None
                

        

