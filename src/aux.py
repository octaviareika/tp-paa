
def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            w, v = map(int, file.readline().split())
            items = []
            for row in file:
                weight, volume, value = map(float, row.strip().split("\t"))
                item = {"weight": weight, "volume":volume, "value":value}
                items.append(item)
            data = {"w": w, "v":v, "items": items}
            return data


        return data

    except Exception as e:
        print(f"Erro ao ler Matriz: {e}")
        return None

def dictionary_creator(max_profit=0, selected_items=None, elapsed_time=0.0):
    if selected_items is None:
        selected_items = []
    return {
        "max_profit": max_profit,
        "selected_items": selected_items,
        "elapsed_time": elapsed_time
    }