
export HASH := $(shell git rev-parse HEAD)

export APP_NAME := SplitCamelCase

run:
	python3 app.py --port $(PORT)

run_default:
	python3 app.py

test:
	python3 app_test.py

setup:
	pip install -r requirements.txt