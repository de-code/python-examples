#!/usr/bin/make -f

VENV = .venv
UV = uv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python

PYTEST_WATCH_MODULES =
ARGS =


venv-clean:
	@if [ -d "$(VENV)" ]; then \
		rm -rf "$(VENV)"; \
	fi

venv-create:
	$(UV) venv

dev-install:
	$(UV) sync

dev-venv: venv-create dev-install


dev-flake8:
	$(PYTHON) -m flake8 python_examples

dev-pylint:
	$(PYTHON) -m pylint python_examples

dev-mypy:
	$(PYTHON) -m mypy --check-untyped-defs python_examples

dev-lint: dev-flake8 dev-pylint dev-mypy


dev-unit-tests:
	$(PYTHON) -m pytest

dev-watch:
	$(PYTHON) -m pytest_watcher \
		--runner=$(VENV)/bin/python \
		. \
		-m pytest -vv $(PYTEST_WATCH_MODULES)


dev-test: dev-lint dev-unit-tests
