# Desafio Dafiti
Uma API simples com Django e DRF para um CRUD de sapatos e um painel administrativo em Django Admin.

## Tecnologias Utilizadas
- Python
- Django/ DRF
- Poetry
- Docker
- Pre-commit
- JWT

## Como rodar o projeto com docker
 - Criar um arquivo .env na raiz:
    ```
    DEBUG=True
    SECRET_KEY="django-insecure-5z0cvtt$%0uekvqztm!ov&95q$l_@k+e6pkno##9+vs)1!%e59"
    DATABASE_URL=postgres://postgres:postgres@db/dafiti_challenge
    ```
- Rodar o docker compose:
    ```
    docker-compose up
    ```

## Como rodar o projeto com poetry
- Criar um arquivo .env na raiz e alterar a config do banco de acordo com sua maquina:
    ```
    DEBUG=True
    SECRET_KEY="django-insecure-5z0cvtt$%0uekvqztm!ov&95q$l_@k+e6pkno##9+vs)1!%e59"
    DATABASE_URL=postgres://postgres:postgres@db/dafiti_challenge
    ```
- Preparando o ambiente:
    ```
    make setup
    ```
- Rodar Migrations:
    ```
    python manage.py migrate
    ```

- Rodar projeto:
    ```
    python manage.py runserver
    ```

## Comandos auxiliares:
- Configurando os hoocks do pre-commit:
	```
    make configure-pre-commit-hook
    ```

- Rodar o lint:
	```
    make lint ou make pre-commit
    ```

- Criar usuário admin no docker (com container em execução):
    ```
    make create-superuser
    ```


#### Observações:
- Na raiz do projeto de um arquivo data.csv de exemplo para subir em lote.
- Todos os endpoints precisam de autenticação JWT, adicionar "Bearer Token" no swagger para funcionar.

- O frontend ficou no Django admin
