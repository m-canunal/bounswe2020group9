# Library imports
import requests

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


def get_news(date):
    params = {
        "q": "Covid",
        "country": "us",
        "from": date,  # example: "2020-05-19"
        "sortBy": "popularity",
        "apiKey": "64508aee042e414b93c1d5b047904c04"
    }
    response = requests.get(
        "http://newsapi.org/v2/top-headlines?",
        params=params
    )
    return response.json()

def get_currencies(date):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"q":"1.0","from":"SGD","to":"MYR"}

    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "c94c624004msh01721a04d9bbbf2p1b6835jsnbe9e5824019f"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text
