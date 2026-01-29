
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
        print(f"Erro ao ler Dados: {e}")
        return None
