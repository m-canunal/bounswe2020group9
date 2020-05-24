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


# return the api of "YYYY-mm-dd"
@app.route("/api/<string:date>")
def get_api(date):
    return jsonify(bazaar_api.get_api(date))

# return the api of today
@app.route("/api")
def get_api_today():
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

# Return the fetched APOD json, day: <string:date>
@app.route("/api/apod/<string:date>")
def api_apod(date):
    return jsonify(api_calls.get_nasa_apod(date))

# Return the fetched APOD json, day: <Today>
@app.route("/api/apod")
def api_apod_today():
    return "Hello World!"
        #jsonify(api_calls.get_nasa_apod(utils.getTodayString()))


# View the Astronomy Picture of the Day: <string:date>
@app.route("/apod/<string:date>")
def apod(date):
    apodJson = api_calls.get_nasa_apod(date)
    if "400, bad request" in apodJson:
        return jsonify(apodJson)
    url = apodJson["url"]
    if "hdurl" in apodJson:
        url = apodJson["hdurl"]
    return render_template("apod.html", url=url)

# View the Astronomy Picture of the Day: <Today>
@app.route("/apod")
def apod_today():
    apodJson = api_calls.get_nasa_apod(utils.getTodayString())
    if "hdurl" in apodJson:
        url = apodJson["hdurl"]
    return render_template("apod.html", url=apodJson["url"])


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"404": "not found"}), 404)

@app.route("/routes")
def routes():
    return jsonify(utils.mainMenu)
# This is here as app.py is our main file
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
