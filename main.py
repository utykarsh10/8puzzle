from board import Board
import numpy as np
import time
from agent import MT, CB, NA, a_star_search

def main():
    seed = 10
    heuristics = [0, MT, CB, NA]

    for m in [10,20,30,40, 50]:
        for heuristic in heuristics:
            expanded_nodes = 0
            
            board = Board(m, seed)
            
            start =  time.perf_counter()
        
            solution, expanded_nodes = a_star_search(board, heuristic)
            correct = board.check_solution(solution)
            if correct:
                print("succeeded")
            else:
                print("failed")
                

            end =  time.perf_counter()
            solution_cpu_time = end-start
            print ("Nodes = " + str(expanded_nodes))
            print(solution_cpu_time)

if __name__ == "__main__":
    main()
