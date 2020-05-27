# Bazaar API Center # 
##  The Documentation ##

##**Base URL = http://127.0.0.1:5000/**


## Getting Covid Results By Date

Takes date as input and returns that day's global and Turkey data.

### URL: "/api/covid
### Method: GET
### Parameters:/{{date}}

### Response:
#### URL:http://127.0.0.1:5000/api/covid/2020-05-25

[{"NewConfirmed":98206,"NewDeaths":3030,"NewRecovered":56379,"TotalConfirmed":5492996,"TotalDeaths":351576,"TotalRecovered":2167913},{"Active":33430,"City":"","CityCode":"","Confirmed":157814,"Country":"Turkey","CountryCode":"TR","Date":"2020-05-25T00:00:00Z","Deaths":4369,"Lat":"38.96","Lon":"35.24","Province":"","Recovered":120015}]

## Getting Weather Results By Date
Takes date as input and returns that day's weather for the user's location.

### URL: "/api/weather
### Method: GET
### Parameters:/{{date}}

### Response:
#### URL:http://127.0.0.1:5000/api/weather/2020-05-24

{
"columns": {
"address": {
"id": "address",
"name": "Address",
"type": 1,
"unit": null
},
"cloudcover": {
"id": "cloudcover",
"name": "Cloud Cover",
"type": 2,
"unit": "%"
},
"conditions": {
"id": "conditions",
"name": "Conditions",
"type": 1,
"unit": null
},
"datetime": {
"id": "datetime",
"name": "Date time",
"type": 3,
"unit": null
},
"dew": {
"id": "dew",
"name": "Dew Point",
"type": 2,
"unit": "degF"
},
"heatindex": {
"id": "heatindex",
"name": "Heat Index",
"type": 2,
"unit": "degF"
},
"humidity": {
"id": "humidity",
"name": "Relative Humidity",
"type": 2,
"unit": "%"
},
"info": {
"id": "info",
"name": "Info",
"type": 1,
"unit": null
},
"latitude": {
"id": "latitude",
"name": "Latitude",
"type": 2,
"unit": null
},
"longitude": {
"id": "longitude",
"name": "Longitude",
"type": 2,
"unit": null
},
"maxt": {
"id": "maxt",
"name": "Maximum Temperature",
"type": 2,
"unit": "degF"
},
"mint": {
"id": "mint",
"name": "Minimum Temperature",
"type": 2,
"unit": "degF"
},
"name": {
"id": "name",
"name": "Name",
"type": 1,
"unit": null
},
"precip": {
"id": "precip",
"name": "Precipitation",
"type": 2,
"unit": "in"
},
"precipcover": {
"id": "precipcover",
"name": "Precipitation Cover",
"type": 2,
"unit": "%"
},
"resolvedAddress": {
"id": "resolvedAddress",
"name": "Resolved Address",
"type": 1,
"unit": null
},
"sealevelpressure": {
"id": "sealevelpressure",
"name": "Sea Level Pressure",
"type": 2,
"unit": "Pa"
},
"snowdepth": {
"id": "snowdepth",
"name": "Snow Depth",
"type": 2,
"unit": "in"
},
"temp": {
"id": "temp",
"name": "Temperature",
"type": 2,
"unit": "degF"
},
"visibility": {
"id": "visibility",
"name": "Visibility",
"type": 2,
"unit": "mi"
},
"wdir": {
"id": "wdir",
"name": "Wind Direction",
"type": 2,
"unit": null
},
"weathertype": {
"id": "weathertype",
"name": "Weather Type",
"type": 1,
"unit": null
},
"wgust": {
"id": "wgust",
"name": "Wind Gust",
"type": 2,
"unit": "mph"
},
"windchill": {
"id": "windchill",
"name": "Wind Chill",
"type": 2,
"unit": "degF"
},
"wspd": {
"id": "wspd",
"name": "Wind Speed",
"type": 2,
"unit": "mph"
}
},
"locations": {
"36.7867,31.4431": {
"address": "36.7867,31.4431",
"alerts": null,
"currentConditions": null,
"distance": 0,
"id": "36.7867,31.4431",
"index": 0,
"latitude": 36.7867,
"longitude": 31.4431,
"name": null,
"stationContributions": null,
"time": 0,
"values": [
{
"cloudcover": null,
"conditions": "",
"datetime": 1590278400000,
"datetimeStr": "2020-05-24T00:00:00+03:00",
"dew": 32.5,
"heatindex": 79.9,
"humidity": 25.93,
"info": null,
"maxt": 82.3,
"mint": 60.7,
"precip": 0,
"precipcover": 0,
"sealevelpressure": null,
"snowdepth": null,
"temp": 70.8,
"visibility": 6.2,
"wdir": 334.58,
"weathertype": "",
"wgust": null,
"windchill": null,
"wspd": 24.2
}
]
}
}
}
