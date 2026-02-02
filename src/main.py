import os
import json
import sys
from functions.backtracking import backtracking_algorithm
from functions.branch_n_bound import bnb_algorithm
from functions.dynamic import dynamic_algorithm
from aux import load_file, run_algorithms, extract_params, calculate_mean, perform_stats, perform_binary_stats

# Aumentar limite de recursão para n=1000
sys.setrecursionlimit(5000)

def main():
    base_dir = "instances"
    summary_results = []
    full_results = [] # Guardaremos o full para o script de análise externa
    
    # Lista e ordena as pastas pelo valor numérico de n e depois W/V
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    folders.sort(key=extract_params)
    
    print(f"Iniciando processamento de {len(folders)} pastas de instâncias...")

    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        instance_files = sorted([f for f in os.listdir(folder_path) if f.startswith("inst_") and f.endswith(".txt")], 
                                key=lambda x: int(x.split('_')[1].split('.')[0]))
        
        print(f"Processando pasta: {folder}")
        
        # Listas para acumular resultados das 10 instâncias
        bt_p, bt_t, bt_c = [], [], []
        bnb_p, bnb_t, bnb_c = [], [], []
        dp_p, dp_t, dp_c = [], [], []
        w_val, v_val, n_val = 0, 0, 0

        for inst_file in instance_files:
            file_path = os.path.join(folder_path, inst_file)
            input_data = load_file(file_path)
            
            if not input_data:
                continue
            
            n_val = len(input_data["items"])
            w_val = input_data["w"]
            v_val = input_data["v"]

            # Executa os algoritmos
            res = run_algorithms(input_data, backtracking_algorithm, bnb_algorithm, dynamic_algorithm)

            # Armazena dados individuais
            bt_p.append(res["bt"]["max_profit"])
            bt_t.append(res["bt"]["elapsed_time"])
            bt_c.append(len(res["bt"]["selected_items"]) if isinstance(res["bt"]["selected_items"], list) else 0)

            bnb_p.append(res["bnb"]["max_profit"])
            bnb_t.append(res["bnb"]["elapsed_time"])
            bnb_c.append(len(res["bnb"]["selected_items"]) if isinstance(res["bnb"]["selected_items"], list) else 0)

            dp_p.append(res["dp"]["max_profit"])
            dp_t.append(res["dp"]["elapsed_time"])
            dp_c.append(len(res["dp"]["selected_items"]) if isinstance(res["dp"]["selected_items"], list) else 0)

            full_results.append({
                "folder": folder, "instance": inst_file, "n": n_val, "W": w_val, "V": v_val,
                "bt_profit": res["bt"]["max_profit"], "bt_time": res["bt"]["elapsed_time"],
                "bnb_profit": res["bnb"]["max_profit"], "bnb_time": res["bnb"]["elapsed_time"],
                "dp_profit": res["dp"]["max_profit"], "dp_time": res["dp"]["elapsed_time"]
            })

        # Calcula as médias e realiza testes estatísticos binários
        summary_results.append({
            "folder": folder, "n": n_val, "W": w_val, "V": v_val,
            "avg_bt_profit": calculate_mean(bt_p), "avg_bt_time": calculate_mean(bt_t), "avg_bt_count": calculate_mean(bt_c),
            "avg_bnb_profit": calculate_mean(bnb_p), "avg_bnb_time": calculate_mean(bnb_t), "avg_bnb_count": calculate_mean(bnb_c),
            "avg_dp_profit": calculate_mean(dp_p), "avg_dp_time": calculate_mean(dp_t), "avg_dp_count": calculate_mean(dp_c),
            
            # Comparações Binárias de Tempo
            "tie_time_bt_bnb": perform_binary_stats(bt_t, bnb_t),
            "tie_time_bt_dp": perform_binary_stats(bt_t, dp_t),
            "tie_time_bnb_dp": perform_binary_stats(bnb_t, dp_t),
            
            # Comparações Binárias de Lucro
            "tie_profit_bt_bnb": perform_binary_stats(bt_p, bnb_p),
            "tie_profit_bt_dp": perform_binary_stats(bt_p, dp_p),
            "tie_profit_bnb_dp": perform_binary_stats(bnb_p, dp_p)
        })

    # Garante que a pasta de resultados existe
    output_dir = "results_analysis"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salva o arquivo JSON dentro da pasta de resultados
    output_path = os.path.join(output_dir, "results_summary.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary_results, f, indent=4, ensure_ascii=False)
    
    print(f"\nConcluído! Resultados salvos em {output_path}")

if __name__ == "__main__":
    main()