from functions.backtracking import backtracking_algorithm
from functions.branch_n_bound import bnb_algorithm
from functions.dynamic import dynamic_algorithm
from aux import load_file
import sys


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    input_data = load_file(file_path)
    
    while input_data is None:
        file_path = input("Insira o caminho correto para o arquivo\n")
        input_data = load_file(file_path)
    

    backtracking_results = backtracking_algorithm(input_data)
    bnb_results = bnb_algorithm(input_data)
    dynamic_results = dynamic_algorithm(input_data)

    print("Backtracking:", backtracking_results)
    print("Branch-and-Bound:", bnb_results)
    print("Dynamic Programming:", dynamic_results)


if __name__ == "__main__":
    main()