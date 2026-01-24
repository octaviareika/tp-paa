import random
import os

def generate_instances(num_items_list, capacities, num_instances=10, folder="instances"):
    os.makedirs(folder, exist_ok=True)
    
    for n_items in num_items_list:
        for W, V in capacities:
            for inst in range(1, num_instances + 1):
                filename = f"{folder}/inst_{n_items}_{W}_{V}_{inst}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"{W}\t{V}\n")
                    for _ in range(n_items):
                        weight = random.randint(1, W)
                        volume = random.randint(1, V)
                        value = round(random.uniform(1, 20), 2)
                        f.write(f"{weight}\t{volume}\t{value}\n")

num_items_list = [5, 10, 15]
capacities = [(10, 9), (20, 15)]
generate_instances(num_items_list, capacities)
