# Проект Api_final
### Описание
Перед Вами API проекта Yatube. Учебный проект Яндекс.Практикум.
Проект ставит перед собой цели создания социальной сети, где у пользователя будет возможность создания личной страницы, публикации записей, просмотр чужих постов и подписки на других авторов, написание комментариев к записям.
Проект реализован через архитектуру SPA. В данной части проекта реализован backend приложения по средствам Django Rest Framework.
Использовано:
* Python v.3.7.5 (https://docs.python.org/3.7/)
* Django v.2.2.16 (https://docs.djangoproject.com/en/2.2/)
* DRF v.3.12.4 (https://www.django-rest-framework.org/community/release-notes/#312x-series)
* Simple JWT v.4.7.2 (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* Flake 8 v.5.0.4 (https://buildmedia.readthedocs.org/media/pdf/flake8/stable/flake8.pdf)

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
Запрос получения списка постов:
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

Запрос добавления комментария:
```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Данные:
```json
{
  "text": "string"
}
```
Ответы:
```
Status code: 200
```
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
```
Status code: 400
```
```json
{
  "text": [
    "Обязательное поле."
  ]
}
```
```
Status code: 401
```
```json
{
  "detail": "Учетные данные не были предоставлены."
}
```
```
Status code: 404
```
```json
{
  "detail": "Страница не найдена."
}
```

Запрос частичного обновления комментария:
```
PATCH http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```
Данные:
```json
{
  "text": "string"
}
```
Ответы:
```
Status code: 200
```
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
```
Status code: 401
```
```json
{
  "detail": "Учетные данные не были предоставлены."
}
```
```
Status code: 403
```
```json
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```
```
Status code: 404
```
```json
{
  "detail": "Страница не найдена."
}
```

Подробная инструкция после установки и запуска проекта по адресу:
[Документация ReDoc](http://127.0.0.1:8000/redoc/)

### Автор:
tlg: @minigraf
e-mail: minigraph@yandex.ru; maikl.nikitin@yahoo.com;
