from board import Board
import numpy as np
import time
from agent import MT, CB, NA, a_star_search

def main():

    #for m in [10,20,30,40,50]:
        #for seed in range(0,10):
            # Sets the seed of the problem so all students solve the same problems
            #board = Board(m, seed)
            
            board = Board(10,21)
            start =  time.process_time()   
           # print(board)
           # print(board.initial_state)
            '''
            ***********************************************
            Solve the Board state here with A*
            ***********************************************
            '''
            print(MT(board))
            print(CB(board))
            print(board)
            print(board.solution)
                    
            #solution = a_star_search(board, 0)
            #correct = board.check_solution(solution)

            #for state in board.next_action_states():
               # print(state[0], state[1])

            end =  time.process_time()
            solution_cpu_time = end-start

if __name__ == "__main__":
    main()
