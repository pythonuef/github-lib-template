.PHONY: install tests lint format coverage clean

install:
	pip install .[dev] && pip install pytest pytest-cov coverage codecov && pip install -e .

lint:
	ruff . && mypy pythonuef_github_lib_template

format:
	black . && ruff --fix .

tests:
	PYTHONPATH=. pytest -v --tb=short tests

coverage:
	PYTHONPATH=. pytest --cov=pythonuef_github_lib_template --cov-report=xml

clean:
	rm -rf dist/ build/ *.egg-info __pycache__ .pytest_cache .mypy_cache