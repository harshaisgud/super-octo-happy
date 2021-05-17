
export HASH := $(shell git rev-parse HEAD)

export APP_NAME := SplitCamelCase

IMAGE_NAME := splitcamelcase
DOCKER_REPOSITORY := harshaisgud
IMAGE := $(DOCKER_REPOSITORY)/$(IMAGE_NAME)

run:
	python3 app.py --port $(PORT)
.PHONY: run

run_default:
	python3 app.py
.PHONY: run_default

test:
	python3 app_test.py
.PHONY: test

setup:
	pip install -r requirements.txt
.PHONY: setup

build:
	docker build . -f Dockerfile -t $(IMAGE):$(HASH) --build-arg GITHASH=$(HASH)
.PHONY: build

push:
	cat .env | docker login --username $(DOCKER_REPOSITORY) --password-stdin
	docker push $(IMAGE):$(HASH)
.PHONY: push