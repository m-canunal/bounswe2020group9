# Library imports
from flask import Flask, render_template, jsonify, make_response, request
import os
from datetime import datetime, timedelta
# Custom files' imports
import api_calls, utils, bazaar_api

# Custom files that we wrote from scratch:
# app.py, api_calls.py, sandbox.py, utils.py, bazaar_api
# Each file has it's description in it

# app.py:
# This page includes the possible routes for the flask app
# Note that main function is in app.py

app = Flask(__name__, static_folder='static', static_url_path='')

# frontend route list:
# / : homepage
# /favicon.ico : icon of homepage


# backend route list:

# /api : return today, everything
# /api/ : return today, everything
# /api/<string:date> : return date, everything

# /api{X_API} : return today, X_API
# /api/{X_API} : return today, X_API
# /api/{X_API}/<string:date> : return date, X_API

# /api/favorites : return favorites
# (everything above are GET requests)
# /api/favorites/add : POST request to favorites, <string:body> will be stored in the array
# /api/favorites/remove : DELETE request to favorites, <string:body> will be deleted if in the array

@app.route("/")
def main_menu():
    return render_template("index.html", today = utils.getTodayString())
@app.route("/old")
def main_menu_old():
    return render_template("menu.html", today = utils.getTodayString())

# will not be used at frontend
'''
@app.route("/api")
@app.route("/api/")
def get_api_today():
    # return the api of today
    return get_api(utils.getTodayString())



# return the api of "YYYY-mm-dd"
@app.route("/api/<string:date>")
def get_api(date):
    return jsonify(bazaar_api.get_api(date))
'''
# return favorites
@app.route("/api/favorites")  # if methods is not given, default is ["GET"]
def api_favorites():
    return jsonify(bazaar_api.favorites)


# add a new favorite
@app.route("/api/favorites/add", methods=["POST"])
def api_favorites_post():
    # request.json is the json object user has given to us
    return jsonify(bazaar_api.favorites_post(str(request.data)[2:-1]))


# delete favorite that is given
@app.route("/api/favorites/remove", methods=["DELETE"])
def api_favorites_delete():
    return jsonify(bazaar_api.favorites_delete(str(request.data)[2:-1]))

@app.route("/api/context")
def api_context():
    return jsonify(api_calls.get_topics(utils.getTodayString()))

#get news about nasa photo
@app.route("/api/news/nasa/<string:date>")
def api_nasa_news(date):
    return jsonify(api_calls.get_nasa_news(date))
# get news
@app.route("/api/news/<string:date>")
def api_news(date):
    response = api_calls.get_news(date)
    """if type(response[0]) is int:
        if response[0][0] == 0:
            response = "Please give a valid date."
        elif response[0][0] == 2:
            response = "No articles about the date specified."""
    return jsonify(response)

@app.route("/api/apod")
@app.route("/api/apod/")
def api_apod_today():
    # return the api of today
    return api_apod(utils.getTodayString())
@app.route("/api/apod/<string:date>")
def api_apod(date):
    # return the api of date
    return jsonify(api_calls.get_nasa_apod(date))

# delete this later, will not be needed in release
@app.route("/apod")
@app.route("/apod/")
def apod_today():
    # View the Astronomy Picture of the Day: <Today>
    return apod(utils.getTodayString())
@app.route("/apod/<string:date>")
def apod(date):
    # View the Astronomy Picture of the Day: "YYYY-mm-dd"
    apodJson = api_calls.get_nasa_apod(date)
    if "400, bad request" in apodJson:
        return jsonify(apodJson)
    url = apodJson["url"]
    if "hdurl" in apodJson:
        url = apodJson["hdurl"]
    return render_template("apod.html", url=url)


# get covid
@app.route("/api/covid")
@app.route("/api/covid/")
def api_covid():
    return jsonify(api_calls.get_covid(utils.getTodayString()))

	#get covid based on date
@app.route("/api/covid/<string:date>")
def api_covid_customDate(date):
    try:
        return jsonify(api_calls.get_covid(date))
    except ValueError:
        return jsonify({"Invalid date": "Try another date"})


#Get Currency exchange rates for today
@app.route("/api/currencies/")
@app.route("/api/currencies")
def api_currenciesToday():
    return jsonify(api_calls.get_currenciesToday())

# get weather api page
@app.route("/api/weather")
@app.route("/api/weather/")
def api_weather():
    return jsonify(api_calls.get_weather_today())


# Return the fetched weather json, day: <string:date>
@app.route("/api/weather/<string:date>")
def weather(date):
    return jsonify(api_calls.get_weather(date))

# Return the fetched weather json, day: today
@app.route("/api/weather/today")
def weather_today():
    return jsonify(api_calls.get_weather_today())

#Get Currency exchange rates for a specific date
@app.route("/api/currencies/<string:date>")
def api_currencies(date):
    return jsonify(api_calls.get_currencies(date))

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