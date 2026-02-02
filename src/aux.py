
def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            first = file.readline().strip()
            if not first:
                raise ValueError("Arquivo vazio ou formato inválido")
            parts = first.split()
            if len(parts) < 2:
                raise ValueError("Cabeçalho deve conter capacidade de peso e volume")
            w_str, v_str = parts[0], parts[1]
            # aceitar inteiros ou floats no arquivo, armazenar capacidades como inteiros
            w = int(float(w_str))
            v = int(float(v_str))

            items = []
            for row in file:
                row = row.strip()
                if not row:
                    continue
                # aceita separador por tabulação ou espaços
                cols = row.split("\t") if "\t" in row else row.split()
                if len(cols) < 3:
                    raise ValueError(f"Linha de item com formato inválido: {row}")
                weight, volume, value = cols[0], cols[1], cols[2]
                item = {"weight": int(float(weight)), "volume": int(float(volume)), "value": float(value)}
                items.append(item)

            data = {"w": w, "v": v, "items": items}
            return data

    except Exception as e:
        print(f"Erro ao ler Dados em {file_path}: {e}")
        return None

def run_algorithms(input_data, bt_func, bnb_func, dp_func):
    """
    Executa os três algoritmos e retorna um dicionário com os resultados filtrados por n.
    """
    n_items = len(input_data["items"])
    
    # Backtracking (n <= 100)
    if n_items <= 250:
        bt_res = bt_func(input_data)
    else:
        bt_res = {"max_profit": "TIMEOUT/SKIPPED", "selected_items": [], "elapsed_time": None}

    # Branch and Bound (n <= 100)
    if n_items <= 1000:
        bnb_res = bnb_func(input_data)
    else:
        bnb_res = {"max_profit": "TIMEOUT/SKIPPED", "selected_items": [], "elapsed_time": None}

    # Dynamic Programming
    try:
        dp_res = dp_func(input_data)
    except Exception as e:
        dp_res = {"max_profit": "ERROR/MEM_LMT", "selected_items": [], "elapsed_time": None}

    return {
        "bt": bt_res,
        "bnb": bnb_res,
        "dp": dp_res
    }

import re
def extract_params(folder_name):
    # Extrai n, W e V do nome da pasta (ex: n100_W20_V20 -> (100, 20, 20))
    match = re.search(r'n(\d+)_W(\d+)_V(\d+)', folder_name)
    if match:
        return tuple(map(int, match.groups()))
    return (0, 0, 0)

def calculate_mean(values):
    # Filtra valores que não são números (strings como "TIMEOUT")
    numeric_values = [v for v in values if isinstance(v, (int, float))]
    if not numeric_values:
        return "N/A"
    return round(sum(numeric_values) / len(numeric_values), 8)

def perform_stats(bt_list, bnb_list, dp_list):
    """
    Verifica se há empate estatístico entre os algoritmos que rodaram.
    Retorna True se houver empate (p-value > 0.05).
    """
    try:
        from scipy import stats
    except ImportError:
        return "N/A (scipy absent)"

    # Filtra apenas os algoritmos que retornaram valores numéricos
    data_to_test = []
    for lst in [bt_list, bnb_list, dp_list]:
        nums = [v for v in lst if isinstance(v, (int, float))]
        if len(nums) == 10: # Só testa se tivermos a amostra completa
            data_to_test.append(nums)
    
    if len(data_to_test) < 2:
        return "N/A (single algo)"

    # Kruskal-Wallis é um teste não-paramétrico ideal para comparar 3 grupos
    try:
        stat, p_value = stats.kruskal(*data_to_test)
        return bool(p_value > 0.05) # Cast para bool nativo do Python
    except Exception:
        return "Error in test"

def perform_binary_stats(list_a, list_b):
    """
    Realiza o teste Mann-Whitney U entre dois grupos.
    Retorna True se houver empate estatístico (p > 0.05).
    """
    try:
        from scipy import stats
    except ImportError:
        return "N/A"

    # Filtra apenas números
    nums_a = [v for v in list_a if isinstance(v, (int, float))]
    nums_b = [v for v in list_b if isinstance(v, (int, float))]

    if len(nums_a) != 10 or len(nums_b) != 10:
        return "N/D" # Dados insuficientes

    try:
        if nums_a == nums_b:
            return True
        _, p_value = stats.mannwhitneyu(nums_a, nums_b)
        return bool(p_value > 0.05) # Cast para bool nativo do Python
    except Exception:
        return "Erro"
