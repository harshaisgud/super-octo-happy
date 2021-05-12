.DEFAULT_GOAL := deploy



export HASH := $(shell git rev-parse HEAD)

export APP_NAME := SUPER-OCTO-HAPPY

run:
	@echo $(value HASH)
	flask run