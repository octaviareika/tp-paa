import random
import os

# Seed fixa para reprodutibilidade
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

def generate_instances(n, W, V, num_instances=10, base_dir="instances"):
    """
    Gera n instâncias de teste para o problema da mochila 0-1 com duas restrições.
    Cria uma pasta específica para a combinação (n, W, V).
    """
    # Cria o nome da pasta para esta combinação
    folder_name = f"n{n}_W{W}_V{V}"
    target_dir = os.path.join(base_dir, folder_name)
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    
    for i in range(1, num_instances + 1):
        filename = f"inst_{i}.txt"
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'w') as f:
            # Primeira linha: Peso Máximo e Volume Máximo
            f.write(f"{W}\t{V}\n")
            for _ in range(n):
                # Peso e Volume gerados aleatoriamente entre 1 e a capacidade máxima
                # Valor gerado aleatoriamente entre 1 e 100
                weight = random.randint(1, W)
                volume = random.randint(1, V)
                value = round(random.uniform(1.0, 100.0), 2)
                f.write(f"{weight}\t{volume}\t{value}\n")
    
    print(f"Geradas 10 instâncias em: {target_dir}")

def main():
    # Listas para iteração (ajuste conforme necessário para sua análise assintótica)
    n_list = [10, 100, 250, 500, 1000]          # Quantidade de itens
    W_list = [0.2, 0.5, 0.8]              # Capacidade de peso (Pequena, Média, Grande) em porcentagem com relação a n, ex: se n = 10, 20 = 2
    V_list = [0.2, 0.5, 0.8]              # Capacidade de volume (Pequena, Média, Grande) em porcentagem com relação a n, ex: se n = 10, 20 = 2

    # Base directory para as instâncias
    base_directory = "instances"

    print(f"Iniciando geração de instâncias com seed: {RANDOM_SEED}")
    
    # Itera sobre todas as combinações
    for n in n_list:
        for i in range(len(W_list)):
            W = int(W_list[i] * n)
            V = int(V_list[i] * n)
            
            generate_instances(n, W, V, num_instances=10, base_dir=base_directory)

    print("\nConcluído! Todas as instâncias foram geradas e organizadas por pasta.")

if __name__ == "__main__":
    main()
