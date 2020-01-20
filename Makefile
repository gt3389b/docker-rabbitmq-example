all:
	docker-compose up --force-recreate --remove-orphans --build --exit-code-from publisher
