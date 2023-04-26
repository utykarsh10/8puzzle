from board import Board
import numpy as np
import time
from agent import MT, CB, NA, a_star_search

def main():
    heuristics = [0, MT, CB, NA]
    heuristicNames = ['BFS', 'MT', 'CB', 'NA']
    heuristicNameCount= 0
    

    for heuristic in heuristics:
        for m in [10,20,30,40,50]:
            correctPercentage = 0
            averageNodes = 0
            averageSolutionTime = 0
            averageSolutionLength = 0
            
            for seed in range(1, 10):
                expanded_nodes = 0
                board = Board(m, seed)
                
                start =  time.perf_counter()
                solution, expanded_nodes = a_star_search(board, heuristic)
                end =  time.perf_counter()
                
                correct = board.check_solution(solution)
                if correct:
                    correctPercentage += 100
                else:
                    correctPercentage += 0
                    
                averageNodes += expanded_nodes
                
                averageSolutionTime += end-start
                
                averageSolutionLength += len(solution)
                
            print("For m = " + str(m) + ", and " + heuristicNames[heuristicNameCount]+ ": ")
            correctPercentage = correctPercentage / 9
            print("Percentage of problems solved: " + str(correctPercentage))
            averageNodes = averageNodes / 9
            print("Average number of search nodes generated: " + str(averageNodes))
            averageSolutionTime = averageSolutionTime / 9
            print("Average CPU time per problem: " + str(averageSolutionTime))
            averageSolutionLength = averageSolutionLength / 9
            print("Average solution length: " + str(averageSolutionLength))
            print(" ")
            
        heuristicNameCount += 1
            

if __name__ == "__main__":
    main()
