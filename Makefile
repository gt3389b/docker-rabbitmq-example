all: up

up:
	docker-compose up \
		--force-recreate \
		--remove-orphans \
		--build \
		--abort-on-container-exit \
		--exit-code-from publisher

stop:
	docker-compose stop

down:
	docker-compose down
