# Проект Api_final
### Описание
Перед Вами API проекта Yatube. Учебный проект Яндекс.Практикум.
Реализовано на Django Rest Framework.
### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/minigraph/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Обновите PIP, дабы избежать ошибок установки зависимостей:

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:
Запрос:
```
GET http://127.0.0.1:8000/api/v1/posts/
```
Ответ:
```
Status code: 200
```
```json
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
    {}
]
}
```

Подробная инструкция после установки и запуска проекта по адресу:
[Документация ReDoc](http://127.0.0.1:8000/redoc/)