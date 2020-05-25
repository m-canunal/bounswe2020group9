# Library imports
import requests
import utils
# Custom files' imports
from flask import jsonify


# Custom files that we write from scratch:
# app.py, api_calls.py, data.py, sandbox.py, utils.py
# Each file has it's description in it

# api_calls.py:
# This page has the functions that will fetch data from other APIs
# Make sure every function's return value is a dictionary

def get_nasa_apod(date):
    params = {
        "api_key": "FbSD5I112W6dykCrvlhXTSKVDpcbY35W4mxFTPCS",
        "date": date
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params
    )
    if response.status_code == 400:
        return {
            "400, bad request": {
                "solution": "please enter a valid date as %Y-%m-%d",
                "example": "2019-02-20"
            }
        }
    return response.json()

def get_nasa_news(date):
    if utils.checkDate(date):
        nasa = get_nasa_apod(date)
        topics = get_topics(date)
        annList = utils.sortByConfidence(topics["annotations"])
        print(annList[0])
        x = 0
        i = 0
        while x == 0:
            params = {
                "q": "\""+annList[i]["spot"]+"\"",
                "language": "en",
                "from": utils.getMaxDate(),
                "sortBy": "popularity",
                "apiKey": "64508aee042e414b93c1d5b047904c04"
            }
            response = requests.get(
                "http://newsapi.org/v2/everything?",
                params=params
            )
            if not response.json()["totalResults"] == 0:
                x = 1
            i += 1
        res = response.json()
        if x == 0:
            res["articles"] = [2]
    else:
        res = {"articles": [0]}
    return res["articles"]

def get_news(date):
    if utils.checkDate(date):
        params = {
            "q": "",
            "country": "us",
            "from": date,  # example: "2020-05-19"
            "sortBy": "popularity",
            "apiKey": "64508aee042e414b93c1d5b047904c04"
        }
        response = requests.get(
            "http://newsapi.org/v2/top-headlines?",
            params=params
        )
        res = response.json()
    else:
        res = {"articles": [0]}
    return res["articles"]
    


def get_topics(date):
    nasa = get_nasa_apod(date)
    params = {
        "text": nasa["explanation"],
        "lang": "en",
        "token": "65bb2b59039e48938896fb18fc547ef6"
    }
    response = requests.get(
        "https://api.dandelion.eu/datatxt/nex/v1",
        params=params
    )
    x=response.json()
    return x
