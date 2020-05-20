from flask import Flask, render_template, jsonify, make_response, abort, request
import requests
import os
import datetime

# Everything started to get messy, comment if possible, assume non-commented parts are just for testing
app = Flask(__name__)

ttd = [
    {'id': 0, 'task': u'Design the system', 'done': True},
    {'id': 1, 'task': u'Write the code', 'done': False},
    {'id': 2, 'taks': u'Write unit tests', 'done': False},
    {'id': 3, 'taks': u'Document the source code', 'done': False},
    {'id': 4, 'taks': u'Review pull requests', 'done': False}
]

# Below used in "/api"
customFav = {0: ["first"], 1: ["second"], 2: ["third"], 3: ["fourth"], 4: ["fifth"], 5: ["sixth"]}
favorites = {"counter": len(customFav), "list": customFav}
# Above used in "/api"

time = datetime.datetime.now()
date = str(time.year) + "-" + str(time.month) + "-" + str(time.day)


@app.route("/")
def mainMenu():
    return jsonify({"routes": {
        "/": {"/": "This Page", "/hello": "Hello World!", "/salih": "SALIH"},
        "/tasks": {
            "/tasks/view": "Tasks, can be updated",
            "/tasks/view/<task_id>": "Get the task:<task_id>",
            "/tasks/create": "Create Task, not available for now"
        },
        "/apod": {
            "/": "Get the Astronomy picture of the day",
            "/<date>": "Get the Astronomy picture of day of the date:<date>"
        },
        "/apodJson": {
            "/": "Get the Json of /apod",
            "/<date>": "Get the Json of /apod/<date>"
        },
        "Errors": {
            "/": {"404": "not found"},
            "/apod": {
                "400, bad request": {
                    "solution": "please enter a valid date as %Y-%m-%d",
                    "example": "2019-02-20"
                }
            }
        }
    }})


# Start of attempt at favorites
@app.route("/api")
def api_list():
    return jsonify(favorites["list"])


@app.route("/api/add", methods=["POST"])
def api_add():
    id = favorites["counter"]
    favorites["list"][id] = request.json
    # counter only increments, ids will always be unique
    favorites["counter"] += 1
    type(favorites["list"])
    print(favorites["list"])
    return jsonify({"POST succesful": favorites["list"]})


@app.route("/api/remove", methods=["DELETE"])
def api_remove():
    try:
        del favorites["list"][request.json[0]]
    except KeyError:
        print(request.json)
        return jsonify({"Error: Key not found": {"Possible solutions": [
            "Make sure you've typed the id as json such that `<json>[0] = id`",
            "Make sure the id you've entered is valid and available"
        ]}})
    return jsonify({"DELETE succesful": favorites["list"]})


# End of attempt at favorites

@app.route("/hello")
def helloWorld():
    return "Hello World!"


@app.route("/news")
def get_news():
    params = {
        "q": "Covid",
        "country": "us",
        "from": "2020-05-19",
        "sortBy": "popularity",
        "apiKey": "64508aee042e414b93c1d5b047904c04"
    }
    response = requests.get(
        "http://newsapi.org/v2/top-headlines?",
        params=params
    )

    x = response.json()
    print(x)
    return x


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


@app.route("/apod")
def nasaApod():
    apodJson = nasaApodJson().json
    if "hdurl" in apodJson:
        return render_template("apod.html", url=apodJson["hdurl"])
    return render_template("apod.html", url=apodJson["url"])


@app.route("/apodJson")
def nasaApodJson():
    params = {
        "api_key": "FbSD5I112W6dykCrvlhXTSKVDpcbY35W4mxFTPCS"
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params
    )
    return jsonify(response.json())


@app.route("/apod/<string:date>")
def nasaApodDate(date):
    apodJson = nasaApodJsonDate(date).json
    if "400, bad request" in apodJson:
        return jsonify(apodJson)
    url = apodJson["url"]
    if "hdurl" in apodJson:
        url = apodJson["hdurl"]
    return render_template("apod.html", url=url)


@app.route("/apodJson/<string:date>", methods=["GET"])
def nasaApodJsonDate(date):
    params = {
        "api_key": "FbSD5I112W6dykCrvlhXTSKVDpcbY35W4mxFTPCS",
        "date": date
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params
    )
    if response.status_code == 400:
        return jsonify({
            "400, bad request": {
                "solution": "please enter a valid date as %Y-%m-%d",
                "example": "2019-02-20"
            }
        })
    return jsonify(response.json())


@app.route("/salih")
def salih():
    return "SALIH"


# Below is the error handlers
@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({"404": "not found"}), 404)


# Above is error handlers

# Below is main
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
# Above is main
