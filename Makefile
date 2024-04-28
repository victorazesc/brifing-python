# Makefile for Django project

# Comandos
PYTHON=python3
PIP=pip3
DJANGO=django-admin
MANAGE=manage.py

# Diretório do ambiente virtual
VENV_DIR=venv

# Comando para iniciar o ambiente virtual
VENV_ACTIVATE=source $(VENV_DIR)/bin/activate

# Comandos de inicialização e execução
RUNSERVER=$(VENV_ACTIVATE) && $(PYTHON) $(MANAGE) runserver
TEST=$(VENV_ACTIVATE) && $(PYTHON) $(MANAGE) test

# Comandos para instalar dependências e criar o ambiente virtual
setup:
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt

# Comando para rodar os testes
test:
	$(TEST)

# Comando para iniciar o servidor de desenvolvimento
run-dev:
	$(RUNSERVER)
run:
	docker-compose up --build -d

run-debug:
	docker-compose -f docker-compose-dev.yaml up --build -d
