
def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            w, v = map(float, file.readline().split())
            items = []
            for row in file:
                weight, volume, value = map(float, row.strip().split("\t"))
                item = {"weight": weight, "volume":volume, "value":value}
                items.append(item)
            data = {"w": w, "v":v, "items": items}
            return data


        return data

    except Exception as e:
        print(f"Erro ao ler Dados: {e}")
        return None
