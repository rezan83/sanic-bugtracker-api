from sanic import Sanic
from sanic.response import json
from sanic_ext import Extend

app = Sanic(__name__)
app.config.CORS_ORIGINS = "*"
Extend(app)


@app.get("/")
async def hello_world(request):
    resp = json({"bugs": "databas"})
    data = [{
            "id": 1,
            "title": "terrible bug",
            "description": "Pineapple button are not responding",
            "solved": False,
            "priority": 3,
            "assignee": "batman",
            "reporter": "superman"
        },
        {
            "id": 2,
            "title": "Banana bug",
            "description": "problem with extension",
            "solved": False,
            "priority": 2,
            "assignee": "batman",
            "reporter": "batman"
        },
        {
            "id": 3,
            "title": "Apple important bug",
            "description": "problem with styling",
            "solved": True,
            "priority": 1,
            "assignee": "robocop",
            "reporter": "robocop"
        },
        {
            "id": 4,
            "title": "terrible Pineapple bug",
            "description": "button are not responding",
            "solved": True,
            "priority": 3,
            "assignee": "batman",
            "reporter": "superman"
        },
        {
            "id": 5,
            "title": "not very bad Orange bug",
            "description": "problem with extension",
            "solved": False,
            "priority": 2,
            "assignee": "batman",
            "reporter": "batman"
        },
        {
            "id": 6,
            "title": "not important bug",
            "description": "problem with styling",
            "solved": False,
            "priority": 1,
            "assignee": "superman",
            "reporter": "robocop"
        },
        {
            "id": 7,
            "title": "terrible Tomato bug",
            "description": "button are not responding",
            "solved": True,
            "priority": 3,
            "assignee": "batman",
            "reporter": "superman"
        },
        {
            "id": 8,
            "title": "not very bad bug",
            "description": "problem with extension",
            "solved": True,
            "priority": 2,
            "assignee": "batman",
            "reporter": "batman"
        },
        {
            "id": 9,
            "title": "not important bug",
            "description": "problem with styling",
            "solved": False,
            "priority": 1,
            "assignee": "superman",
            "reporter": "robocop"
        },
        {
            "id": 10,
            "title": "terrible bug",
            "description": "button are not responding",
            "solved": False,
            "priority": 3,
            "assignee": "batman",
            "reporter": "superman"
        },
        {
            "id": 11,
            "title": "not very bad bug",
            "description": "problem with extension",
            "solved": False,
            "priority": 2,
            "assignee": "batman",
            "reporter": "batman"
        },
        {
            "id": 12,
            "title": "not Tomato bug",
            "description": "problem with styling",
            "solved": False,
            "priority": 1,
            "assignee": "superman",
            "reporter": "robocop"
        },
        {
            "id": 13,
            "title": "terrible bug",
            "description": "button are not responding",
            "solved": False,
            "priority": 3,
            "assignee": "batman",
            "reporter": "superman"
        },
        {
            "id": 14,
            "title": "not Tomato bad bug",
            "description": "problem with extension",
            "solved": False,
            "priority": 2,
            "assignee": "batman",
            "reporter": "batman"
        },
        {
            "id": 15,
            "title": "not important bug",
            "description": "problem with styling",
            "solved": True,
            "priority": 1,
            "assignee": "superman",
            "reporter": "robocop"
        },
        {
            "id": 16,
            "title": "Banana bug",
            "description": "button are not responding",
            "solved": False,
            "priority": 3,
            "assignee": "batman",
            "reporter": "superman"
        },
        {
            "id": 17,
            "title": "not very bad bug",
            "description": "problem with extension",
            "solved": False,
            "priority": 2,
            "assignee": "robocop",
            "reporter": "batman"
        },
        {
            "id": 18,
            "title": "not important bug",
            "description": "problem with styling",
            "solved": False,
            "priority": 1,
            "assignee": "superman",
            "reporter": "robocop"
        },
        {
            "id": 19,
            "title": "not Apple bad bug",
            "description": "problem with extension",
            "solved": True,
            "priority": 2,
            "assignee": "robocop",
            "reporter": "batman"
        },
        {
            "id": 20,
            "title": "not Orange bug",
            "description": "problem with styling",
            "solved": False,
            "priority": 1,
            "assignee": "superman",
            "reporter": "robocop"
        }]
    resp.set_body(data)
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)