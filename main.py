from board import Board
import numpy as np
import time
from agent import MT, CB, NA, a_star_search

# https://www.statology.org/jaccard-similarity-python/
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
                print("For " + str(m) + ", succeeded with 100%")
            else:
                print("For " + str(m) + ", failed")
                correct_solution, not_relevant = a_star_search(board, CB)
                numCorrectMove = 0;
                for i in range(len(correct_solution)):
                    if solution[i] == correct_solution[i]:
                        numCorrectMove += 1;
                    else:
                        break
                percentage = numCorrectMove / len(correct_solution) * 100
                print ("For " + str(m) + ", " + str(percentage) + "% was correct")
            print ("For " + str(m) + ": Nodes = " + str(expanded_nodes))
            
            solution_cpu_time = end-start
            print("For " + str(m) + ": the average CPU time is: " + str(solution_cpu_time))
            
            solution_length = len(solution)
            print("The length of the array is:", solution_length)
            print(" ")
            

if __name__ == "__main__":
    main()
