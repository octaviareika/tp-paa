import time

def dynamic_algorithm(data):
    start = time.time()

    max_profit, selected_items = dynamic_function(data)

    end = time.time()
    total_time = end - start

    return_dictionary = {
        "max_profit": max_profit,
        "selected_items": selected_items,
        "elapsed_time": total_time,
    } 

    return return_dictionary


# Função para implementação, deve retornar o lucro e uma lista com os itens contidos na melhor solução, inclua os parâmetros necessários
def dynamic_function(data):
    W = int(data["w"])
    V = int(data["v"])
    items = data["items"]
    n = len(items)

    # Inicializando a tabela DP
    # usar float para valores (podem ser não-inteiros)
    dp = [[[0.0 for _ in range(V + 1)]
                for _ in range(W + 1)]
                for _ in range(n + 1)]

    # Preenchendo a tabela DP
    for i in range(1, n + 1):
        wi = int(items[i - 1]["weight"])
        li = int(items[i - 1]["volume"])
        vi = float(items[i - 1]["value"])

        for ww in range(W + 1):
            for vv in range(V + 1):
                # inicialmente não pegar o i-ésimo item
                dp[i][ww][vv] = dp[i - 1][ww][vv]

                if ww >= wi and vv >= li:
                    candidate = dp[i - 1][ww - wi][vv - li] + vi
                    if candidate > dp[i][ww][vv]:
                        dp[i][ww][vv] = candidate

    
    # Backtracking para identificar os itens usados
    selected_items = []
    cur_w = W
    cur_v = V

    for i in range(n, 0, -1):
        if dp[i][cur_w][cur_v] != dp[i - 1][cur_w][cur_v]:  # Item i foi escolhido
            selected_items.append(i - 1)
            wi = int(items[i - 1]["weight"])
            li = int(items[i - 1]["volume"])
            cur_w -= wi
            cur_v -= li

    selected_items.reverse()

    return dp[n][W][V], selected_items
