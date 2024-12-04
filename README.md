
# term_test_task
(Тестовое задание)

## Для запуска проекта:

### Windows

1) Установите и активируйте виртуальное окружение:

```cmd
python -m venv venv
```
```cmd
venv\Scripts\activate
```

2) Установите зависимости:
```cmd
pip install -r requirements.txt
```

3) Выполните миграции:
```cmd
python manage.py makemigrations
```
```cmd
python manage.py migrate
```

4) Запустите сервер:
```cmd
python manage.py runserver
```

5) Перейдите в web-приложение в браузере:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

6) Для создания суперпользователя:
```cmd
python manage.py createsuperuser
```

---

### macOS/Linux

1) Установите и активируйте виртуальное окружение:

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

2) Установите зависимости:
```bash
pip install -r requirements.txt
```

3) Выполните миграции:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

4) Запустите сервер:
```bash
python manage.py runserver
```

5) Перейдите в web-приложение в браузере:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

6) Для создания суперпользователя:
```bash
python manage.py createsuperuser
```

