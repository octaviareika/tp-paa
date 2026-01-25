import time

def backtracking_algorithm(data):
    start = time.time()

    max_profit, selected_items = backtracking_function(data)

    end = time.time()
    total_time = end - start

    return_dictionary = {
        "max_profit": max_profit,
        "selected_items": selected_items,
        "elapsed_time": total_time,
    } 

    return return_dictionary


# Função para implementação, deve retornar o lucro e uma lista com os itens contidos na melhor solução, inclua os parâmetros necessários
def backtracking_function(data):
    best_result = {
        "max_profit": 0,
        "selected_items": None
    }

    W = data["w"]
    V = data["v"]
    items = data["items"]
    n = len(items)

    def backtrack(index=0, current_weight=0, current_volume=0, current_profit=0, current_items=None):
        if current_items is None:
            current_items = []
        
        if index == n:
            if current_profit > best_result["max_profit"]:
                best_result["max_profit"] = current_profit
                best_result["selected_items"]= current_items.copy()
            return
        
        current_item = items[index]

        if current_weight + current_item["weight"] <= W and current_volume + current_item["volume"] <= V:
            current_items.append(index)
            backtrack(
                index= index+1,
                current_weight= current_weight + current_item["weight"], 
                current_volume= current_volume + current_item["volume"], 
                current_profit= current_profit + current_item["value"], 
                current_items = current_items
            )
            current_items.pop()
        
        backtrack(
                index= index+1,
                current_weight= current_weight, 
                current_volume= current_volume, 
                current_profit= current_profit, 
                current_items = current_items
        )


    backtrack()
    return best_result["max_profit"], best_result["selected_items"]