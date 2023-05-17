include .env
export .env

migrations:
	bash -c "python manage.py makemigrations"

migrate:
	bash -c "python manage.py migrate"

runserver:
	bash -c "python manage.py runserver"

test-migrate-db:
	bash -c "python manage.py migrate --database test"

test:
	bash -c "python manage.py test"

load-data:
	./scripts/load-initial-data.sh