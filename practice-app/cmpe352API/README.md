# Bazaar API Center # 
##  The Documentation ##

##**Base URL = 127....**


## Getting Covid Results By Date

Takes date as input and returns that day's global and Turkey data.

###URL: "/api/covid
###Method: GET
###Parameters:/{{date}}

###Response:
####URL:http://127.0.0.1:5000/api/covid/2020-05-25

[{"NewConfirmed":98206,"NewDeaths":3030,"NewRecovered":56379,"TotalConfirmed":5492996,"TotalDeaths":351576,"TotalRecovered":2167913},{"Active":33430,"City":"","CityCode":"","Confirmed":157814,"Country":"Turkey","CountryCode":"TR","Date":"2020-05-25T00:00:00Z","Deaths":4369,"Lat":"38.96","Lon":"35.24","Province":"","Recovered":120015}]

