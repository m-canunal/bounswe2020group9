# Library imports
from flask import Flask, jsonify, abort, request

# Custom files that we write from scratch:
# app.py, api_calls.py, data.py, sandbox.py, utils.py
# Each file has it's description in it

# sandbox.py:
# This page is the place for stuff that we will not use, but we might need later

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello World!"


@app.route("/salih")
def salih():
    return "SALIH"


# ttd, example used in class.
ttd = [
    {'id': 0, 'task': u'Design the system', 'done': True},
    {'id': 1, 'task': u'Write the code', 'done': False},
    {'id': 2, 'taks': u'Write unit tests', 'done': False},
    {'id': 3, 'taks': u'Document the source code', 'done': False},
    {'id': 4, 'taks': u'Review pull requests', 'done': False}
]


@app.route("/tasks/view", methods=["GET"])
def get_tasks():
    return jsonify({"things-to-do": ttd})


@app.route("/tasks/view/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = [task for task in ttd if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})


@app.route("/tasks/create", methods=["POST"])
def create_tasks():
    if not request.json or not "task" in request.json:
        abort(400)
    print(request.json)
    return ("DONE!")
