# Library imports
from flask import Flask, render_template, jsonify, make_response, request
import os
# Custom files' imports
import api_calls, utils, bazaar_api

# Custom files that we wrote from scratch:
# app.py, api_calls.py, sandbox.py, utils.py, bazaar_api
# Each file has it's description in it

# app.py:
# This page includes the possible routes for the flask app
# Note that main function is in app.py

app = Flask(__name__)


@app.route("/")
def main_menu():
    return render_template("menu.html")


@app.route("/api")
def get_api():
    if request.args.get("date"):
    # return the api of "YYYY-mm-dd"
        return jsonify(bazaar_api.get_api(request.args.get("date")))
    # else return the api of today
    return jsonify(bazaar_api.get_api(utils.getTodayString()))




# return favorites
@app.route("/api/favorites")  # if methods is not given, default is ["GET"]
def api_favorites():
    return jsonify(bazaar_api.favorites)


# add a new favorite
@app.route("/api/favorites/add", methods=["POST"])
def api_favorites_post():
    # request.json is the json object user has given to us
    return jsonify(bazaar_api.favorites_post(request.json))


# delete favorite<id>
@app.route("/api/favorites/remove", methods=["DELETE"])
def api_favorites_delete():
    return jsonify(bazaar_api.favorites_delete(request.json[0]))

# get news
@app.route("/api/news")
def api_news():
    return jsonify(api_calls.get_news(utils.getTodayString()))

@app.route("/api/apod")
def api_apod():
    if request.args.get("date"):
    # return the api of "YYYY-mm-dd"
        return jsonify(api_calls.get_nasa_apod(request.args.get("date")))
    # return the api of today
    return jsonify(api_calls.get_nasa_apod(utils.getTodayString()))

@app.route("/apod")
def apod_today():
    if request.args.get("date"):
    # View the Astronomy Picture of the Day: "YYYY-mm-dd"
        apodJson = api_calls.get_nasa_apod(request.args.get("date"))
    else:
    # View the Astronomy Picture of the Day: <Today>
        apodJson = api_calls.get_nasa_apod(utils.getTodayString())
    if "400, bad request" in apodJson:
        return jsonify(apodJson)
    url = apodJson["url"]
    if "hdurl" in apodJson:
        url = apodJson["hdurl"]
    return render_template("apod.html", url=url)


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"404": "Not Found"}), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({"500": "Internal Server Error"}), 500)

# This is here as app.py is our main file
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
