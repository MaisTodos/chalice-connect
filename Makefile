close:
	@echo "--> Close Docker."
	docker-compose down


develop:
	@echo "--> Creating Docker."
	docker-compose build --no-cache

bash:
		docker-compose run api bash

delete:
	docker-compose run --rm api chalice chalice delete $(env)

deploy:
	docker-compose run --rm api chalice deploy $(env)
