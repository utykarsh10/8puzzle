from board import Board
import numpy as np
import time
from agent import MT, CB, NA, a_star_search

def main():
    seed = 10
    heuristics = [0, MT, CB, NA]

    for m in [10,15,20,25]:
        for heuristic in heuristics:
            
            board = Board(m, seed)
            
            start =  time.perf_counter()
            
            time_limit = 5
        
            solution, expanded_nodes = a_star_search(board, heuristic, time_limit)
            correct = board.check_solution(solution)

            end =  time.perf_counter()
            solution_cpu_time = end-start
            print(solution_cpu_time)

if __name__ == "__main__":
    main()
