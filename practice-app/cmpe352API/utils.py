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
    if (date.month<10):
        return str(date.year) + "-0" + str(date.month) + "-" + str(date.day)
    return str(date.year) + "-" + str(date.month)+ "-" + str(date.day)

def sortByConfidence(annList):
    retList =sorted(annList, key = lambda i: i['confidence'], reverse = True)
    return retList

def getFreeID(dictionary):
    # Gets dictionary as input, returns the first integer that is not being used
    # Used in data.api["favorites"] to fina a free slot
    key = 0
    while key in dict.keys(dictionary):
        key += 1
    return key

def checkInputFormat(date):
    if len(date) == 10:
        year = date[0:4]
        char1 = date[4]
        month = date[5:7]
        char2 = date[7]
        day = date[8:]
        if (year.isnumeric()) and (char1 =="-") and (month.isnumeric()) and (char2 =="-") and (day.isnumeric()) :
            return True
        else:
            return False
    else:
        return False


def checkDate(dateString):
    maxDateString = getMaxDate()
    lastMaxIndex = maxDateString.rfind('-')
    lastDateIndex = dateString.rfind('-')
    date = datetime.datetime(int(dateString[0:4]), int(dateString[5:lastDateIndex]), int(dateString[lastDateIndex+1:]))
    maxDate = datetime.datetime(int(maxDateString[0:4]), int(maxDateString[5:lastMaxIndex]), int(maxDateString[lastMaxIndex + 1:]))
    if date < maxDate:
        return False
    else:
        return True

def getMaxDate():
    time = datetime.datetime.now()
    if time.day==31:
        return str(time.year) + "-" + str(time.month) + "-" + str(time.day-30)
    else:
        if time.month==1:
            return str(time.year-1) + "-" + str(12) + "-" + str(time.day+1)
        elif time.month ==3:
            if time.year % 4 ==0:
                return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day-1)
            else:
                return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day-2)
        elif time.month <=7:
            if time.month % 2 == 0:
                return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day+1)
            else:
                return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day)
        elif time.month==8:
            return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day+1)
        else:
            if time.month % 2 == 0:
                return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day)
            else:
                return str(time.year) + "-" + str(time.month-1) + "-" + str(time.day+1)