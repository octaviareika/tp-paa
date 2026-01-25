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
    return max_profit, selected_items