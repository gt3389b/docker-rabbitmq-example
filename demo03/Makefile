all: up

up:
	docker-compose up \
		--force-recreate \
		--remove-orphans \
		--build \
		--abort-on-container-exit \
		--scale consumer=4 \
		--exit-code-from publisher

stop:
	docker-compose stop

down:
	docker-compose down
