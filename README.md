## Запуск:

```bash
git clone https://github.com/allelleo/TeskTaskHelikonCmpany
```

```bash
cd TeskTaskHelikonCmpany
```

```bash
docker-compose up -d
```

---

get - http://localhost:8000/task/ - Получение всех задач
***
get - http://localhost:8000/task/6/ - Получение одной задачи ( 6 - id задачи)
***
delete - http://127.0.0.1:8000/task/destroy/ - Удаление задачи (надо в body передать task_id)
***
post - http://localhost:8000/task/ - создание задачи
отправлять это:

```json
{
	"deadline": "2024-02-29",
	"executor": "2",
	"priority": 2,
	"title": "Task 21",
	"description": "bla bla",
	"projects": [1]
}
```

P.S. Надо чтобы был executor создан и проекты к которым цепляются задачи, делайте это через админку ибо в тз неписалось про api для создания этих сущностей :)
***
post - http://localhost:8000/task/1/ - обновление задачи ( 1 - id задачи)
отправлять это:

```json
{
	"deadline": "2024-02-29",
	"executor": "2",
	"priority": 2,
	"title": "Task 21",
	"description": "bla bla",
	"projects": [1]
}
```

P.S. Надо чтобы был executor создан и проекты к которым цепляются задачи, делайте это через админку ибо в тз неписалось про api для создания этих сущностей :)
P.S. №2 - Можно обновить как и все поля так и какие-то отдельно, не обязательно отправлять все
***
P.S. № Последний - Первые 2 API - в подарок
