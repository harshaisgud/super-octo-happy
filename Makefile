.DEFAULT_GOAL := deploy

export HASH=$(git rev-parse HEAD)
export APP_NAME=SUPER-OCTO-HAPPY

run:
	@echo $(value HASH)
	python3 app.py