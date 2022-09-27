setup:
	poetry shell
	poetry install

configure-pre-commit-hook:
	poetry run pre-commit install

lint or pre-commit:
	poetry run pre-commit run -a

create-superuser:
	docker-compose exec dafiti_challenge python manage.py createsuperuser
