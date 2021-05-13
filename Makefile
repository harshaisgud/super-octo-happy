.DEFAULT_GOAL := deploy



export HASH := $(shell git rev-parse HEAD)

export APP_NAME := SplitCamelCase

run:
	python3 app.py --port 3000

test:
	python3 app_test.py