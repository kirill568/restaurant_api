## Как запустить  
1. Выполните команду `poetry shell`
2. Выполните команду `uvicorn app.main:app --port 9000 --reload`
3. Откройте браузер по адресу `http://127.0.0.1:9000`
  

## Как запустить docker стэк
1. Установите [docker](https://docs.docker.com/engine/install/)
2. В корне проекта создайте копию файла `.env.example` с именем `.env`
3. Выполните команду `docker compose build`
4. Выполните команду `docker compose up`
5. Примените миграции `docker compose exec web poetry run alembic upgrade head`
6. Откройте браузер по адресу `http://127.0.0.1:9000`