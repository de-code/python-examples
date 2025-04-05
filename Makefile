#!/usr/bin/make -f

VENV = venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python


venv-clean:
	@if [ -d "$(VENV)" ]; then \
		rm -rf "$(VENV)"; \
	fi

venv-create:
	python3 -m venv $(VENV)

dev-install:
	$(PIP) install --disable-pip-version-check -r requirements.build.txt
	$(PIP) install --disable-pip-version-check \
		-r requirements.txt \
		-r requirements.dev.txt
	$(PIP) install -e .

dev-venv: venv-create dev-install


dev-flake8:
	$(PYTHON) -m flake8 ai

dev-pylint:
	$(PYTHON) -m pylint ai

dev-mypy:
	$(PYTHON) -m mypy --check-untyped-defs ai

dev-lint: dev-flake8 dev-pylint dev-mypy


dev-start-telemetry-server:
	$(PYTHON) -m phoenix.server.main serve
