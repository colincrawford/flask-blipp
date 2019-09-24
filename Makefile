.PHONY: test test-ci coverage coverage-ci lint format

test:
	poetry run pytest -vv

coverage:
	poetry run pytest --cov=flask_blipp .

test-ci:
	poetry run pytest -vv \
	--junit-xml=test-reports/pytest/junit.xml \
	--cov=flask_blipp \
	--cov-report \
	html:coverage/cov_html .

lint:
	poetry run pycodestyle --config .pycodestyle.ini .

format:
	poetry run black .
