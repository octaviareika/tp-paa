import time


def bnb_algorithm(data):
    start = time.perf_counter()

    max_profit, selected_items = bnb_function(data)

    end = time.perf_counter()
    total_time = end - start

    return_dictionary = {
        "max_profit": max_profit,
        "selected_items": selected_items,
        "elapsed_time": total_time,
    } 

    return return_dictionary

def greedy_initial_solution(indexed, W, V):
    temp_w, temp_v, temp_profit = W, V, 0.0
    temp_items = []
    for i, wi, li, vi in indexed:
        if wi <= temp_w and li <= temp_v:
            temp_w -= wi
            temp_v -= li
            temp_profit += vi
            temp_items.append(i)
    return temp_profit, temp_items, temp_w, temp_v

# Função para implementação, deve retornar o lucro e uma lista com os itens contidos na melhor solução, inclua os parâmetros necessários
def bnb_function(data):
    W = int(data["w"])
    V = int(data["v"])
    items = data["items"]
    n = len(items)

    # indexed list: (original_index, weight, volume, value)
    indexed = [
        (i, int(items[i]["weight"]), int(items[i]["volume"]), float(items[i]["value"]))
        for i in range(n)
    ]

    # ordenar por heurística: valor / (peso + volume)
    indexed.sort(key=lambda x: x[3] / (x[1] + x[2]) if (x[1] + x[2]) > 0 else float('inf'), reverse=True)

    best_profit = 0.0
    best_items = []

    best_profit, best_items, rem_w_init, rem_v_init = greedy_initial_solution(indexed, W, V)

    # Bound via relaxação fracionária (respeitando ambas capacidades)
    def fractional_bound(idx, rem_w, rem_v, acc_profit):
        bound = acc_profit
        for j in range(idx, n):
            _, wi, li, vi = indexed[j]
            if wi <= rem_w and li <= rem_v:
                rem_w -= wi
                rem_v -= li
                bound += vi
            else:
                # fração limitada pelo menor recurso disponível relativo
                frac_w = rem_w / wi if wi > 0 else 0.0
                frac_v = rem_v / li if li > 0 else 0.0
                frac = max(frac_w, frac_v)
                bound += vi * frac
                break
        return bound

    # DFS com poda por bound
    def dfs(idx, rem_w, rem_v, acc_profit, chosen):
        nonlocal best_profit, best_items
        if idx >= n:
            if acc_profit > best_profit:
                best_profit = acc_profit
                best_items = chosen.copy()
            return

        ub = fractional_bound(idx, rem_w, rem_v, acc_profit)
        if ub <= best_profit:
            return

        i, wi, li, vi = indexed[idx]

        # tentar incluir o item
        if wi <= rem_w and li <= rem_v:
            chosen.append(i)
            dfs(idx + 1, rem_w - wi, rem_v - li, acc_profit + vi, chosen)
            chosen.pop()

        # tentar não incluir
        dfs(idx + 1, rem_w, rem_v, acc_profit, chosen)

    dfs(0, W, V, 0.0, [])

    best_items.sort()
    return best_profit, best_items
