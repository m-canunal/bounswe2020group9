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


# The Json on the main menu, it has no use at all
mainMenu = {"routes": {
    "/": {"/": "This Page", "/hello": "Hello World!", "/salih": "SALIH"},
    "/tasks": {
        "/tasks/view": "Tasks, can be updated",
        "/tasks/view/<task_id>": "Get the task:<task_id>",
        "/tasks/create": "Create Task, not available for now"
    },
    "/apod": {
        "/": "Get the Astronomy picture of the day",
        "/<date>": "Get the Astronomy picture of day of the date:<date>"
    },
    "/apodJson": {
        "/": "Get the Json of /apod",
        "/<date>": "Get the Json of /apod/<date>"
    },
    "Errors": {
        "/": {"404": "not found"},
        "/apod": {
            "400, bad request": {
                "solution": "please enter a valid date as %Y-%m-%d",
                "example": "2019-02-20"
            }
        }
    }
}}
