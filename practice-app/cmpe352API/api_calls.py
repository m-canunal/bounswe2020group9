# Library imports
import requests

import covid
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
    if utils.checkInputFormat(date):
        if utils.checkDate(date) == "valid":
            nasa = get_nasa_apod(date)
            topics = get_topics(date)
            annList = utils.sortByConfidence(topics["annotations"])
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
                res["articles"] = ["No articles about the date specified."]
        else:
            res = {"articles": ["Please give a valid date."]}
    else:
        res ={"articles": ["Wrong input format"]}
    return res["articles"]

def get_news(date):
    if utils.checkInputFormat(date):
        if utils.checkDate(date) == "valid":
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
            res = {"articles": ["Please give a valid date."]}
    else:
        res ={"articles": ["Wrong input format"]}
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

    return response.json()


#get latest currency rates
def get_currenciesToday():
    url = "https://api.exchangeratesapi.io/latest"
    querystring = {"base":"TRY", "symbols": "USD,GBP,EUR,CAD" }
    response = requests.request("GET", url, params=querystring)
    return response.json()

#get currency rates for a specific date
def get_currencies(date):  # example: "2020-05-19"
    url = "https://api.exchangeratesapi.io/"+date
    querystring = {"base":"TRY", "symbols": "USD,GBP,EUR,CAD"}
    response = requests.request("GET", url, params=querystring)
    return response.json()

def get_covid(date):
    return covid.getGlobalAndTurkeysDataByDate(date)

