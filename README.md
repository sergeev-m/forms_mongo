# forms/mongodb

Web-приложение для определения заполненных форм.  
В базе данных хранится список шаблонов форм

В ответе возвращает имя шаблона формы, если поля формы совпали с полями в 
присланной форме. Совпадающими считаются поля, у которых совпали имя и тип
значения. Полей в пришедшей форме может быть больше чем в шаблоне.

Если подходящей формы не нашлось, вернуть ответ в следующем формате

```
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
```

### Пример шаблона формы:
```json
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```
### типы полей:
* email
* телефон
* дата
* текст.

###  Пример запроса:
```
/get_form POST
f_name1=value1&f_name2=value2
```
  
## Старт

```bash
git@github.com:sergeev-m/forms_mongo.git

# Переименовать .env.example на .env

docker-compose up

# восстановить бд.
docker exec -it forms_mongo mongorestore /mongo_dump -u <username> -p <passord>

# скрипт. тестовые запросы.
docker exec -it forms python tests/test.py

```

## Используемы инструменты

- python - 3.11
- FastApi
- MongoDB - 7
- docker compose - 3.9

***

### Контакты

Михаил  
[email](server-15@yandex.ru)  
[telegram](https://t.me/sergeev_mikhail)
