import json
import os

def generate_graphs_and_tables(output_dir="results_analysis"):
    summary_file = os.path.join(output_dir, "results_summary.json")
    
    if not os.path.exists(summary_file):
        summary_file = "results_summary.json"

    if not os.path.exists(summary_file):
        print(f"Erro: {summary_file} não encontrado. Execute a main.py primeiro.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(summary_file, 'r') as f:
        data = json.load(f)

    # Ordenação garantida para evitar linhas cruzadas
    data.sort(key=lambda d: (d['n'], d['W'], d['V']))

    # Labels completos para as tabelas e simplificados para os gráficos
    labels_full = [f"n={d['n']} | W={d['W']} | V={d['V']}" for d in data]
    labels_graph = [f"n{d['n']}\nW{d['W']}\nV{d['V']}" for d in data] 
    
    # 1. Tabelas Markdown (Nomes Completos e Formatação Limpa)
    generate_comparative_table(data, "Comparação de Tempo de Execução (s)", 
                             ["avg_bt_time", "avg_bnb_time", "avg_dp_time"], 
                             os.path.join(output_dir, "tabela_tempo.md"))
    
    generate_comparative_table(data, "Comparação de Lucro Máximo", 
                             ["avg_bt_profit", "avg_bnb_profit", "avg_dp_profit"], 
                             os.path.join(output_dir, "tabela_lucro.md"))
    
    generate_comparative_table(data, "Média de Itens Selecionados", 
                             ["avg_bt_count", "avg_bnb_count", "avg_dp_count"], 
                             os.path.join(output_dir, "tabela_itens.md"))

    generate_stat_table(data, os.path.join(output_dir, "tabela_estatistica.md"))

    # 2. Gráficos (Estética Equilibrada e Corrigida)
    try:
        import matplotlib.pyplot as plt
        import matplotlib.ticker as ticker
        
        # Coleta de dados
        bt_t = [val_or_zero(d['avg_bt_time']) for d in data]
        bnb_t = [val_or_zero(d['avg_bnb_time']) for d in data]
        dp_t = [val_or_zero(d['avg_dp_time']) for d in data]

        bt_p = [val_or_zero(d['avg_bt_profit']) for d in data]
        bnb_p = [val_or_zero(d['avg_bnb_profit']) for d in data]
        dp_p = [val_or_zero(d['avg_dp_profit']) for d in data]

        bt_c = [val_or_zero(d['avg_bt_count']) for d in data]
        bnb_c = [val_or_zero(d['avg_bnb_count']) for d in data]
        dp_c = [val_or_zero(d['avg_dp_count']) for d in data]

        algos = ['Backtracking', 'Branch and Bound', 'Programação Dinâmica']

        # Gráfico de Tempo (Escala Logarítmica)
        save_plot(plt, labels_graph, [bt_t, bnb_t, dp_t], algos, 
                  "Tempo Médio de Execução (Escala Logarítmica)", "Tempo (s)", 
                  os.path.join(output_dir, "grafico_tempo.png"), log_scale=True)

        # Gráfico de Lucro
        save_plot(plt, labels_graph, [bt_p, bnb_p, dp_p], algos, 
                  "Lucro Máximo Médio", "Lucro", 
                  os.path.join(output_dir, "grafico_lucro.png"))

        # Gráfico de Itens (Média de produtos na mochila)
        save_plot(plt, labels_graph, [bt_c, bnb_c, dp_c], algos, 
                  "Média de Itens na Mochila", "Quantidade de Itens", 
                  os.path.join(output_dir, "grafico_itens.png"))
        
        print(f"✅ Gráficos corrigidos e salvos em: {output_dir}")

    except ImportError:
        print("\n⚠️ Aviso: Matplotlib não encontrado.")

def val_or_zero(v):
    return v if isinstance(v, (int, float)) else 0

def generate_comparative_table(data, title, keys, filename):
    content = f"# {title}\n\n"
    content += "| Entrada (n, W, V) | Backtracking | Branch and Bound | Programação Dinâmica |\n"
    content += "| :--- | :---: | :---: | :---: |\n"
    for d in data:
        row_label = f"**n={d['n']}** | W={d['W']}, V={d['V']}"
        v_bt = f"{d.get(keys[0], 'N/A')}"
        v_bnb = f"{d.get(keys[1], 'N/A')}"
        v_dp = f"{d.get(keys[2], 'N/A')}"
        content += f"| {row_label} | {v_bt} | {v_bnb} | {v_dp} |\n"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)

def generate_stat_table(data, filename):
    content = "# Análise de Empate Estatístico (Tempo)\n\n"
    content += "| n | Backtracking vs Branch and Bound | Backtracking vs Prog. Dinâmica | Branch and Bound vs Prog. Dinâmica |\n"
    content += "| :--- | :---: | :---: | :---: |\n"
    for d in data:
        row_label = f"**n={d['n']}**"
        t1 = "Empate" if d.get('tie_time_bt_bnb') == True else "Dif"
        t2 = "Empate" if d.get('tie_time_bt_dp') == True else "Dif"
        t3 = "Empate" if d.get('tie_time_bnb_dp') == True else "Dif"
        content += f"| {row_label} | {t1} | {t2} | {t3} |\n"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)

def save_plot(plt, x, y_list, labels_list, title, ylabel, filename, scientific=False, log_scale=False):
    plt.figure(figsize=(10, 6))
    
    colors = ['#e41a1c', '#377eb8', '#4daf4a'] # Cores nítidas e clássicas
    markers = ['o', 's', '^']

    indices = list(range(len(x)))

    for y, label, color, marker in zip(y_list, labels_list, colors, markers):
        # Filtra apenas pontos válidos
        # Para escala logarítmica, v deve ser estritamente maior que 0
        if log_scale:
            valid_idx = [i for i, v in enumerate(y) if v > 0]
        else:
            valid_idx = [i for i, v in enumerate(y) if v > 0 or (v == 0 and "time" not in filename)]
            
        if valid_idx:
            # Usamos os índices para garantir a ordem correta das linhas
            sorted_idx = sorted(valid_idx)
            plt.plot([indices[i] for i in sorted_idx], [y[i] for i in sorted_idx], 
                     marker=marker, label=label, color=color, 
                     linewidth=1.8, markersize=7, alpha=0.9)
    
    if log_scale:
        plt.yscale('log')
        plt.grid(True, which="both", linestyle='--', alpha=0.5)
    elif scientific:
        plt.gca().ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.grid(True, linestyle='--', alpha=0.7)
    else:
        plt.grid(True, linestyle='--', alpha=0.7)

    plt.title(title, fontsize=14, fontweight='bold', pad=15)
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel("Configurações das Instâncias", fontsize=12)
    
    # Define os labels do eixo X usando os índices numéricos
    plt.xticks(indices, x, rotation=0, fontsize=9)
    
    plt.legend(loc='best', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

if __name__ == "__main__":
    generate_graphs_and_tables()
