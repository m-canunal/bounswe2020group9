import requests
import json

def getCasesByCountryAndDate(country,date):
	fromString=date+"T00:00:00Z"
	toString=date+"T00:00:01Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/country/"+country+"?"
	response=requests.get(url,params=params)
	print(response.json())

getCasesByCountryAndDate("italy","2020-05-23")


def getAllCountriesByDate(date):
	fromString=date+"T00:00:00Z"
	toString="2020-08-01T00:00:01Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/world?"
	response=requests.get(url,params=params)

	print(response.json()[0])

getAllCountriesByDate("2020-05-02")

def getTurkeyByDate(date):
	fromString=date+"T00:00:00Z"
	toString=date+"T00:00:01Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/country/turkey?"
	response=requests.get(url,params=params)
	print(response.json())

getTurkeyByDate("2020-05-23")