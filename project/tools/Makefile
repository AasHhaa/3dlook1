build:
	@docker-compose build

down:
	@docker-compose down

stop:
	@docker-compose stop

clean: stop # add '--rmi all' for remove containers
	@docker-compose  down --remove-orphans -v

up:
	@docker-compose up

reboot:
	@docker-compose stop && docker-compose up

quick-start:
	@docker-compose build && docker-compose up

migrate:
	@docker-compose run 3dlook_api python manage.py migrate

makemigrate:
	@docker-compose run 3dlook_api python manage.py makemigrations

bash-api:
	@docker exec -it 3dlook_api bash

bash-db:
	@docker exec -it postgres_db_3dlook bash

test:
	@docker-compose run 3dlook_api python manage.py test
