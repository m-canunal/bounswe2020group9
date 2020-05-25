import requests
import json
import unittest
from datetime import datetime, timedelta


def getCasesByCountryAndDate(country,date):
	fromString=date+"T00:00:00Z"
	toString=date+"T00:00:01Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/country/"+country+"?"
	response=requests.get(url,params=params)
	return response.json()

#print(getCasesByCountryAndDate("italy","2020-05-23"))


def getAllCountriesByDate(date):
	fromString=date+"T00:00:00Z"
	incrementedDate=(datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
	print(incrementedDate)
	toString=incrementedDate+"T00:00:00Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/world?"
	response=requests.get(url,params=params)

	return response.json()

#print(getAllCountriesByDate("2020-05-02"))

def getTurkeyByDate(date):
	fromString=date+"T00:00:00Z"
	toString=date+"T00:00:01Z"
	params = {
		"from": fromString,
		"to": toString
	}
	
	url="https://api.covid19api.com/country/turkey?"
	response=requests.get(url,params=params)
	return response.json()

#print(getTurkeyByDate("2020-05-23"))


def getGlobalAndTurkeysDataByDate(date):
	globalData=getAllCountriesByDate(date)
	turkeyData=getTurkeyByDate(date)
	globalData+=turkeyData
	return globalData

#print(getGlobalAndTurkeysDataByDate("2020-05-23"))


class Test_Covid19_API(unittest.TestCase):
    def test_api(self):
        country= "germany"
        data="2020-05-23"
        results = getCasesByCountryAndDate(country,data)
        if(results is not None):
        	self.assertTrue("Country" in results[0])
        	self.assertTrue("CountryCode" in results[0])
        	self.assertTrue("Province" in results[0])
        	self.assertTrue("City" in results[0])
        	self.assertTrue("CityCode" in results[0])
        	self.assertTrue("Lat" in results[0])
        	self.assertTrue("Lon" in results[0])
        	self.assertTrue("Confirmed" in results[0])
        	self.assertTrue("Date" in results[0])
		
    def test_the_result(self):
        country= "germany"
        data="2020-05-23"
        self.assertTrue(getCasesByCountryAndDate(country,data))
                        
if(__name__ == "__main__"):
    unittest.main()
