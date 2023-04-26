from board import Board
import numpy as np
import time
from agent import MT, CB, NA, a_star_search

def calculate_similarity(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity * 100

def main():
    seed = 10
    heuristics = [0, MT, CB, NA]

    for m in [10,20,30,40, 50]:
        for heuristic in heuristics:
            expanded_nodes = 0
            
            board = Board(m, seed)
            
            start =  time.perf_counter()
            solution, expanded_nodes = a_star_search(board, heuristic)
            end =  time.perf_counter()
            
            correct = board.check_solution(solution)
            if correct:
                print("succeeded with 100%")
            else:
                print("failed")
                correct_solution, not_needed = a_star_search(board, NA)
                correctness = calculate_similarity(solution, correct_solution)
                
            print("Percentage of correctness: " + str(correctness))
            print ("Nodes = " + str(expanded_nodes))
            solution_cpu_time = end-start
            print(solution_cpu_time)

if __name__ == "__main__":
    main()
