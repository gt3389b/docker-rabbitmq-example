all: up

up:
	docker-compose up \
		--force-recreate \
		--remove-orphans \
		--build \
		--abort-on-container-exit \
		--exit-code-from consumer

stop:
	docker-compose stop

down:
	docker-compose down
