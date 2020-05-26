# Library imports
from flask import jsonify, render_template

# Custom files' imports
import api_calls, utils

# Custom files that we wrote from scratch:
# app.py, api_calls.py, sandbox.py, utils.py, bazaar_api
# Each file has it's description in it

# bazaar_api.py:
# This page includes the necessary functions of the API we submit
# All return types should be dictionary


# Things that will be hold in  app.get_api()
favorites = ["1999-06-21", "2012-09-20", "2017-07-26", "2002-01-17"]


# Get api depending on date
def get_api(date):
    api = {"favorites": favorites,
        "news" : api_calls.get_news(date),
        "apod" : api_calls.get_nasa_apod(date),
        "nasa-news": api_calls.get_nasa_news(date)
        # add more if necessary
    }
    return api


# Functions to modify favorites
def favorites_post(input):
    if not input:
        input = utils.getTodayString()
    if input in favorites:
        return{
            "Duplicate error" : "Date \"" + input + "\" already Favorite"
        }
    else:
        favorites.append(input)
    return {"POST succesful": favorites}


def favorites_delete(id):
    try:
        favorites.remove(id)
        return {"DELETE succesful": favorites}
    except ValueError :
        return {
            "Error: Key not found": {"Possible solutions": [
            "ALERT, THESE SOLUTIONS NEED REVIEW",
            "Make sure you've typed the id as json such that `<json>[0] = id`",
            "Make sure the id you've entered is valid and available"
        ]}}