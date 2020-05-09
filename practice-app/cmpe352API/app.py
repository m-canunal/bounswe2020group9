from flask import Flask, render_template, jsonify, make_response, abort, request
import requests
import os

app = Flask(__name__)

ttd = [
    {'id': 0,'task': u'Design the system','done': True},
    {'id': 1,'task': u'Write the code','done': False},
    {'id': 2,'taks': u'Write unit tests','done': False},
    {'id': 3,'taks': u'Document the source code','done': False},
    {'id': 4,'taks': u'Review pull requests','done': False}
]
nasaFav = [
    {}
]



@app.route("/")
def mainMenu():
    return jsonify({"routes":{
            "/":{"/":"This Page", "/hello": "Hello World!", "/salih": "SALIH"},
            "/tasks":{
                "/tasks/view": "Tasks, can be updated",
                "/tasks/view/<task_id>": "Get the task:<task_id>",
                "/tasks/create":"Create Task, not available for now"
            },
            "/apod":{
                "/":"Get the Astronomy picture of the day",
                "/<date>":"Get the Astronomy picture of day of the date:<date>"
            },
            "/apodJson":{
                "/":"Get the Json of /apod",
                "/<date>":"Get the Json of /apod/<date>"
            },
            "Errors":{
                "/":{"404":"not found"},
                "/apod":{
                    "400, bad request": {
                        "solution": "please enter a valid date as %Y-%m-%d",
                        "example": "2019-02-20"
                    }
                }
            }
    }})

@app.route("/hello")
def helloWorld():
    return "Hello World!"
@app.route("/tasks/view", methods=["GET"])
def get_tasks():
 return jsonify({"things-to-do": ttd})
@app.route("/tasks/view/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = [task for task in ttd if task["id"] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({"task":task[0]})
@app.route("/tasks/create", methods=["POST"])
def create_tasks():
    if not request.json or not "task" in request.json:
        abort(400)

@app.route("/apod")
def nasaApod():
    apodJson = nasaApodJson().json
    if "hdurl" in apodJson:
        return render_template("apod.html", url=apodJson["hdurl"])
    return render_template("apod.html", url=apodJson["url"])
@app.route("/apodJson")
def nasaApodJson():
    params={
        "api_key":"FbSD5I112W6dykCrvlhXTSKVDpcbY35W4mxFTPCS"
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
    url=apodJson["url"]
    if "hdurl" in apodJson:
        url=apodJson["hdurl"]
    return render_template("apod.html", url=url)
@app.route("/apodJson/<string:date>", methods=["GET"])
def nasaApodJsonDate(date):
    params={
        "api_key":"FbSD5I112W6dykCrvlhXTSKVDpcbY35W4mxFTPCS",
        "date":date
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params
    )
    if response.status_code==400:
        return jsonify({
            "400, bad request":{
                "solution":"please enter a valid date as %Y-%m-%d",
                "example":"2019-02-20"
            }
        })
    return jsonify(response.json())

@app.route("/salih")
def salih():
    return "SALIH"

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({"404":"not found"}),404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
