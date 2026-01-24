from functions.backtracking import backtracking_algorithm
from functions.branch_n_bound import bnb_algorithm
from functions.dynamic import dynamic_algorithm
from aux import load_file
import sysarg


def main():
    if len(sysarg.argv) != 2:
        print("Uso: python main.py <file_path>")
        sys.exit(1)
    
    file_path = sysarg.argv[1]
    
    input_data = load_file(file_path)
    
    while input_data is None:
        file_path = input("Insira o caminho correto para o arquivo\n")
        input_data = load_file(file_path)
    

    backtracking_results = backtracking_algorithm(input_data)
    bnb_results = bnb_algorithm(input_data)
    dynamic_results = dynamic_algorithm(input_data)


if __name__ == "__main__":
    main()