# Makefile para o Jogo RPG (corrigido para jogo.py)

GREEN = \033[0;32m
RED = \033[0;31m
YELLOW = \033[1;33m
NC = \033[0m

PROGRAM = jogo.py  # ← Alterado de main.py para jogo.py
VENV_DIR = venv

.PHONY: help
help:
	@echo "$(GREEN)📚 Comandos disponíveis:$(NC)"
	@echo ""
	@echo "  make setup    - Instalar dependências no venv"
	@echo "  make run      - Executar o jogo"
	@echo "  make clean    - Limpar arquivos temporários"
	@echo "  make venv     - Criar ambiente virtual (se não existir)"
	@echo ""

.PHONY: venv
venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "$(GREEN)Criando ambiente virtual...$(NC)"; \
		python3 -m venv $(VENV_DIR); \
		echo "$(GREEN)✅ Venv criado!$(NC)"; \
	else \
		echo "$(GREEN)✅ Venv já existe$(NC)"; \
	fi

.PHONY: setup
setup: venv
	@echo "$(GREEN)Instalando dependências...$(NC)"
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install colorama pygame
	@echo "$(GREEN)✅ Dependências instaladas!$(NC)"

.PHONY: run
run:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "$(RED)❌ Venv não encontrado. Execute: make setup$(NC)"; \
		exit 1; \
	fi
	@echo "$(GREEN)Iniciando o jogo...$(NC)"
	@if [ ! -d "sons" ]; then \
		mkdir -p sons; \
		echo "$(YELLOW)⚠️  Pasta 'sons' criada$(NC)"; \
	fi
	$(VENV_DIR)/bin/python $(PROGRAM)

.PHONY: clean
clean:
	@echo "$(GREEN)Limpando arquivos temporários...$(NC)"
	rm -rf __pycache__
	rm -rf *.pyc
	@echo "$(GREEN)✅ Limpeza concluída!$(NC)"

.PHONY: clean-venv
clean-venv:
	@echo "$(GREEN)Removendo ambiente virtual...$(NC)"
	rm -rf $(VENV_DIR)
	@echo "$(GREEN)✅ Venv removido!$(NC)"

.PHONY: reinstall
reinstall: clean-venv setup

.DEFAULT_GOAL := help