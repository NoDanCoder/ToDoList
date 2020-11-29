# ToDo List

ToDo is a Django project for dealing with organization tasks, enable you create your own tasks and set deadlines.

## Description

This project allows you to create tasks to keep organized your job, you only have to get into the web, then lookup in navbar the 'create task' button. App will redirect you to a form that allows you to create a new tasks with this fields

- Title (unique)
- Description
- Estimated Time
- Worked Time

If fields are filled correctly you'll be redirect to main page, where you can relize your task has been add to a table. Now, if you have worked in your tasks, you would like to update ```Worked Time``` field, you can make that through edit button next to every list task, then simply put time you'd like to append to this field and select ```Send Change``` option.

## Installation

First clone repo.

```bash
git clone https://github.com/NoDanCoder/ToDoList.git
cd ToDoList
```
I reccomend you setup first your virtual environment.
```bash
python3 -m venv .env
source .env/bin/activate
```
Then import dependences.
```bash
pip install wheel
pip install -r requirements.txt
```
Now make DB migrations and run!
```bash
python manage.py migrate
python manage.py runserver
```
You can connect directly through localhost
```bash
localhost:8000/
```
## Usage

As programmer you would be interested to add this app to your setup with other automation tools, well, there's a API REST where you can create your tasks from third party apps. Example:

```HTTP
POST /api/create/ HTTP/1.1
Content-Type: application/jsonl; charset=utf-8...

{
    "title": "Finish templates",
    "description": "Deadline is close so first...",
    "estimated_time": 162,
    "worked_time": 21.16
}
```

And your response if data is OK:
```HTTP
HTTP/1.1 201 CREATED
Content-Type: ...

{
    "title": "Finish templates",
    "description": "Deadline is close so first...",
    "estimated_time": 162,
    "worked_time": 21.16
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
