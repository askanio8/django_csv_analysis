UID := $(shell id -u)

# Note: Get env variables from .env file
#include .env

.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-configs &&\
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp .env.example .env &&\
	cp compose.override.dev.yaml compose.override.yaml


.PHONY: d-run
# Just run
d-run:
	@export UID=${UID} &&\
	COMPOSE_PROFILES=full_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up \
			--build


.PHONY: d-run-i-local-dev
# Just run services for local development. For example, Database, Redis, etc.
d-run-i-local-dev:
	@export UID=${UID} &&\
	COMPOSE_PROFILES=local_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose \
			up --build \


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@export UID=${UID} &&\
	COMPOSE_PROFILES=full_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@make poetry-install && \
	pre-commit install

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python main.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye
