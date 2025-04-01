Установка и запуск
------------------

* Переходим в директорию проекта

```shell
cd interview_drf
```

* Создаем файл .env такой же, как .env.example (меняем настройки при необходимости)

```shell
touch .env
```

* Создаем виртуальное окружение

```shell
python3 -m venv venv
```

* Активируем виртуальное окружение или [запускаем с помощью docker-compose](#docker)

```shell
source venv/bin/activate
```

* Устанавливаем зависимости

```shell
pip install -r requirements.txt
```

* Выполняем миграции

```shell
python3 manage.py migrate
```

* Собираем статику

```shell
python3 manage.py collectstatic
```

* Создать суперпользователя
```
python3 manage.py create_admin
```

* Запуск

```shell
python3 manage.py runserver
```