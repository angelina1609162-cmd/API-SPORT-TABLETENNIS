.PHONY: build up down shell install

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

shell:
	docker compose exec api /bin/bash

install:
	python -m pip install -r requirements.txt
