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
    dp = [[[0 for _ in range(V + 1)]
                for _ in range(W + 1)]
                for _ in range(n + 1)]

    # Preenchendo a tabela DP
    for i in range(1, n + 1):
        wi = int(items[i - 1]["weight"])
        li = int(items[i - 1]["volume"])
        vi = items[i - 1]["value"]

        for w in range(W + 1):
            for v in range(V + 1):
                dp[i][w][v] = dp[i - 1][w][v]

                if w >= wi and v >= li:
                    dp[i][w][v] = max(dp[i][w][v], dp[i - 1][w - wi][v - li] + vi)

    
    # Backtraking para identificar a rota que foi utilizada
    selected_items = []
    w = w
    v = V

    for i in range(n, 0, -1):
        if dp[i][w][v] != dp[i - 1][w][v]: # Item i foi escolhido
            selected_items.append(i - 1)
            wi = int(items[i - 1]["weight"])
            li = int(items[i - 1]["volume"])
            w -= wi
            v -= li

    selected_items.reverse()

    return dp[n][W][V], selected_items
