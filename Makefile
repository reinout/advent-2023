install: venv
	venv/bin/pip install -r requirements.txt
	venv/bin/pip install -e .

venv:
	python3 -m venv venv

test:
	venv/bin/pytest

check:
	ruff check . --fix

beautiful:
	ruff format .
