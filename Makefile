
install:
	poetry install

test:
	poetry run pytest tests -vv

test-coverage:
	poetry run pytest --cov=sales_report_generator --cov-report xml tests/

lint:
	poetry run flake8 sales_report_generator

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test test-coverage lint selfcheck check build publish package-install
