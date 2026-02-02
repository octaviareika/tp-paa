# TP-PAA: Análise de Algoritmos para o Problema da Mochila

Este projeto foi desenvolvido para a disciplina de **Projeto e Análise de Algoritmos (PAA)**. O objetivo principal é implementar, testar e analisar o desempenho de diferentes abordagens algorítmicas para resolver o **Problema da Mochila****.

## 🚀 Algoritmos Implementados

O projeto compara três abordagens clássicas:

1.  **Programação Dinâmica**: Solução ótima utilizando subproblemas sobrepostos.
2.  **Backtracking**: Exploração exaustiva do espaço de estados com podas.
3.  **Branch and Bound**: Técnica de busca em árvore com limites para otimização da exploração.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Bibliotecas de Análise:** `pandas`, `numpy`, `matplotlib`
- **Automação:** `Makefile`

## 📂 Estrutura do Projeto

```text
tp-paa/
├── src/
│   ├── main.py              # Script principal de execução dos experimentos
│   ├── aux.py               # Funções auxiliares e limites de execução
│   └── functions/           # Implementação dos algoritmos
│       ├── backtracking.py
│       ├── branch_n_bound.py
│       └── dynamic.py
├── generate_instances.py    # Gerador de instâncias de teste
├── analyze_results.py       # Script para geração de gráficos e tabelas
├── instances/               # Diretório (gerado) com arquivos de entrada
├── results_analysis/        # Diretório (gerado) com gráficos e relatórios
├── Makefile                 # Automação de todo o pipeline
└── requirements.txt         # Dependências do projeto
```

## ⚙️ Como Executar

O projeto utiliza um `Makefile` para simplificar a execução de todo o pipeline de experimentação.

### 1. Preparar o Ambiente

Recomenda-se o uso de um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # No Linux/macOS
pip install -r requirements.txt
```

### 2. Rodar o Pipeline Completo

Para gerar instâncias, executar os algoritmos e gerar as análises estatísticas automaticamente, basta rodar:

```bash
make
```

### 3. Comandos Individuais

- `make instances`: Apenas gera novas instâncias de teste.
- `make run_experiment`: Executa os algoritmos nas instâncias geradas.
- `make analyze`: Gera os gráficos e tabelas a partir dos resultados salvos.
- `make clean`: Remove arquivos temporários, instâncias e resultados anteriores.

## 📊 Resultados e Análise

Após a execução do pipeline (`make`), os resultados estarão disponíveis na pasta `results_analysis/`, incluindo:
- Gráficos de tempo de execução (em escala logarítmica).
- Comparação de complexidade empírica.
- Tabelas detalhadas de performance por tamanho de instância.
