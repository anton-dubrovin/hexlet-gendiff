install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

setup: install build package-install