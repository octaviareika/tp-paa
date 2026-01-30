from functions.backtracking import backtracking_algorithm
from functions.branch_n_bound import bnb_algorithm
from functions.dynamic import dynamic_algorithm
from aux import load_file
import sys


def main():
    
    for i in range(10):

        input_data = load_file(f"../input_files/instances/instance_{i+1}.txt")

        backtracking_results = backtracking_algorithm(input_data)
        bnb_results = bnb_algorithm(input_data)
        dynamic_results = dynamic_algorithm(input_data)

        print(f"Arquivo instance_{i+1}:\n")

        print("Backtracking:", backtracking_results)
        print("Branch-and-Bound:", bnb_results)
        print("Dynamic Programming:", dynamic_results)
        
        print()




if __name__ == "__main__":
    main()