import requests
import json

def getCasesByCountryAndDate(country,date):
	fromString=date+"T00:00:00Z"
	toString=date+"T00:00:01Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/total/country/"+country+"/status/confirmed?"
	response=requests.get(url,params=params)
	print(response.json()[0]['Cases'])

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
	
	url="https://api.covid19api.com/total/country/turkey/status/confirmed?"
	response=requests.get(url,params=params)
	print(response.json()[0]['Cases'])

getTurkeyByDate("2020-05-23")