# HRBuilder
![HRBuilder]

# Стек технологий
<div id="badges" align="center">
  <img src="https://img.shields.io/badge/Python%203.11-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
  <img src="https://img.shields.io/badge/FastAPI%20-white?style=for-the-badge&logo=fastapi&"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
</div>

# Описание проекта



### Логирование.

### Версионирование.

## Запуск проекта посредством Docker.
### Клонировать репозиторий и перейти в него в командной строке.
```
https://github.com/voronovdaniil/HRBuilder.git
``` 
- Перейти в ветку develop.
```
git checkout develop
```
- Перейти в папку infra.
```
cd infra
```
- Запустить  docker-compose
```
docker-compose up -d
```
- Создать миграции
```
docker-compose exec backend alembic revision --autogenerate -m "Migration name"
```
- Применить миграции
```
docker-compose exec backend alembic upgrade head
```
# Документация API первой версии будет доступна по адресу.
```
http://localhost/docs/
``` 
## Установка проекта из репозитория  GitHub.
### Установить Python 3.11
- Для Windows https://www.python.org/downloads/
- Для Linux 
```
sudo apt update
sudo apt -y install python3-pip
sudo apt install python3.11
``` 
### Клонировать репозиторий и перейти в него в командной строке.
```
https://github.com/voronovdaniil/HRBuilder.git
``` 
## Запуск проекта.
###  Развернуть виртуальное окружение.
```
python -m venv venv
``` 
 - для Windows;
```
venv\Scripts\activate.bat
``` 
 - для Linux и MacOS.
``` 
source venv/bin/activate
``` 
### Установить систему контроля зависимостей Poetry
```
pip install poetry
``` 
### Установить зависимости
```
poetry install
``` 
### Установка .pre-commit hook
```
pre-commit install
``` 
### Команды для создания миграций
```
alembic revision --autogenerate -m "Migration name"
``` 
### Команды для применения миграций
```
alembic upgrade head
```
### Запуск проекта
- В файле .env заполнить данные БД и секрета. Пример заполнения.
```
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password123
DB_HOST=db
DB_PORT=5432
SECRET=moi_secret123123123123
``` 
- Запустить main.py
