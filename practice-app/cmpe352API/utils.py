# Library imports
import datetime


# Custom files that we write from scratch:
# app.py, api_calls.py, data.py, sandbox.py, utils.py
# Each file has it's description in it

# utils.py:
# This page has the general functions/variables we've implemented

def getTodayString():
    # Returns today as a string in "YYYY-mm-dd" format
    # Used multiple times in api_calls
    date = datetime.datetime.now()
    return str(date.year) + "-" + str(date.month) + "-" + str(date.day)


def getFreeID(dictionary):
    # Gets dictionary as input, returns the first integer that is not being used
    # Used in data.api["favorites"] to fina a free slot
    key = 0
    while key in dict.keys(dictionary):
        key += 1
    return key


# The Json on the main menu
mainMenu = {
    "Main Menu": {
        "Possible routes that are available": {
            "/": "This Page",
            "/apod": {
                "/apod": "apod.html with the Astronomical Picture of the Day of today",
                "/apod/<string:Date>": "apod.html with the Astronomical Picture of the Day of <Date>",
            },
            "/api/apod": {
                "/api/apod": "Get the \"Astronomical Picture of the Day API\" of today",
                "/api/apod/<string:Date>": "Get the \"Astronomical Picture of the Day API\" of <Date>",
            },
            "/api/favorites": {
                "/api/favorites": "GET the favorites",
                "/api/favorites/add": "POST a json into favorites",
                "/api/favorites/remove": "REMOVE an id from favorites"
            },
            "/api/news": {
                "/api/news": "Get the \"news API\" of today",
                "/api/news/<string:Date>": "Get the \"news API\" of <Date>",
            },
            "Errors": {
                "/": {"404": "not found"},
            }
        }
    }
}
