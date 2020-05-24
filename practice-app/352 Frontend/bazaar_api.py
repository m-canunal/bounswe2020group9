# Library imports
from flask import jsonify

# Custom files' imports
import api_calls, utils

# Custom files that we wrote from scratch:
# app.py, api_calls.py, sandbox.py, utils.py, bazaar_api
# Each file has it's description in it

# bazaar_api.py:
# This page includes the necessary functions of the API we submit
# All return types should be dictionary


# Things that will be hold in  app.get_api()
favorites = {0: ["first"], 1: ["second"], 2: ["third"], 3: ["fourth"], 4: ["fifth"], 5: ["sixth"]}


# Get api depending on date
def get_api(date):
    api = {"favorites": favorites}
    api["news"] = api_calls.get_news(date)
    api["apod"] = api_calls.get_nasa_apod(date)
    # add more if necessary
    return api


# Functions to modify favorites
def favorites_post(input):
    favorites[utils.getFreeID(favorites)] = input
    return {"POST succesful": favorites}


def favorites_delete(id):
    try:
        del favorites[id]
    except KeyError:
        return {"Error: Key not found": {"Possible solutions": [
            "Make sure you've typed the id as json such that `<json>[0] = id`",
            "Make sure the id you've entered is valid and available"
        ]}}
    return {"DELETE succesful": favorites}