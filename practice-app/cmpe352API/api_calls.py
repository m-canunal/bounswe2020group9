# Library imports
import requests, utils, geocoder

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

# alcan & hasan was here
def get_weather(date):
    g = geocoder.ip('me')
    location=g.latlng
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=24&startDateTime="+date+"T00:00:00&endDateTime="+date+"T23:59:59&unitGroup=us&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location="+str(location[0])+","+str(location[1])+"&key=7ITZ7NZ04VSIKZBKADNHGZ1UJ"
    return requests.get(url).json()

def get_weather_today():
    g = geocoder.ip('me')
    location=g.latlng
    today=utils.getTodayString()
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=24&startDateTime="+today+"T00:00:00&endDateTime="+today+"T23:59:59&unitGroup=us&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location="+str(location[0])+","+str(location[1])+"&key=7ITZ7NZ04VSIKZBKADNHGZ1UJ"
    return requests.get(url).json()

    