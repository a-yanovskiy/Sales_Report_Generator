install:
	@poetry install

test:
	poetry run pytest sales_report_generator tests

lint:
	poetry run flake8 sales_report_generator

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
