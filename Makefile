# Variáveis
PYTHON = python3
PIP = pip3
RM = rm -rf

# Alvo padrão
all: run

# 1. Gera as instâncias (limpa as antigas primeiro)
instances:
	@echo "Limpando instâncias antigas e gerando novas..."
	$(RM) instances/
	$(PYTHON) generate_instances.py

# 2. Executa o experimento principal (main.py)
run_experiment: instances
	@echo "Executando os algoritmos nas instâncias..."
	$(PYTHON) src/main.py

# 3. Gera gráficos e tabelas
analyze: run_experiment
	@echo "Gerando análises estatísticas e gráficos..."
	$(PYTHON) analyze_results.py

# Atalho para rodar o pipeline completo
run: analyze
	@echo "\nPipeline concluído com sucesso!"
	@echo "Todos os resultados foram salvos na pasta 'results_analysis/'"

# Limpa todos os arquivos gerados
clean:
	@echo "Limpando diretório do projeto..."
	$(RM) instances/
	$(RM) results_summary.json
	$(RM) results_analysis/
	$(RM) src/__pycache__
	$(RM) src/functions/__pycache__

.PHONY: all instances run_experiment analyze run clean
