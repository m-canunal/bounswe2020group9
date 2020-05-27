# Bazaar API Center # 
##  The Documentation ##

## **Base URL = http://127.0.0.1:5000/**


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

## Getting Top Tech News by Date

Takes date as input and returns top technology news from US in English between 1 month ago and the specified date.

### URL: "/api/news
### Method: GET
### Parameters:/{{date}}

### Response:
#### URL:http://127.0.0.1:5000/api/news/2020-05-16

[
    {
        "author": "Cointelegraph By Samuel Haig",
        "content": "Ripple partner and investor, SBI Holdings, announced plans to integrate Ripple-powered settlements across ATMs in Japan.\r\nThe news was revealed in SBI’s latest financial report, announcing a plan to … [+1513 chars]",
        "description": "SBI wants to use Ripple-powered settlement to make it easier for Japanese consumers to access funds regardless of banking affiliation",
        "publishedAt": "2020-05-17T00:00:00Z",
        "source": {
            "id": null,
            "name": "Cointelegraph"
        },
        "title": "Ripple Settlements Are Coming to Japanese ATMs",
        "url": "https://cointelegraph.com/news/ripple-settlements-are-coming-to-japanese-atms",
        "urlToImage": "https://s3.cointelegraph.com/storage/uploads/view/d664f5a8d9dd58a7aae4efbef4f312cc.jpg"
    },
    {
        "author": "By Claire Mitzel claire.mitzel@roanoke.com 981-3334",
        "content": "Earlier this school year, Elizabeth Rice, 12, stood up in her James Madison Middle School classroom to present a project on a planet.\r\nElizabeth has Down syndrome, and because different little things… [+13627 chars]",
        "description": "Educators, bracing for learning loss when students return to the classroom, are trying to minimize disruption to learning and mitigate exacerbated inequities.",
        "publishedAt": "2020-05-17T00:00:00Z",
        "source": {
            "id": null,
            "name": "Roanoke Times"
        },
        "title": "Emergency distance learning shows value of support, stability in the classroom",
        "url": "https://www.roanoke.com/news/education/emergency-distance-learning-shows-value-of-support-stability-in-the-classroom/article_38d9a77d-ee39-5b6e-b76c-c2c4ba80ba73.html",
        "urlToImage": "https://bloximages.newyork1.vip.townnews.com/roanoke.com/content/tncms/assets/v3/editorial/d/d1/dd19a728-ddfd-5d2b-a12a-45c74d7390ad/5ebdacc103149.image.jpg?crop=1763%2C992%2C0%2C91&resize=1120%2C630&order=crop%2Cresize"
    },
    {
        "author": "Cameron Thibos, Liliane Mouan, Simon Massey",
        "content": "Migration from Africa to Europe has, since the long summer of migration in 2015, been at the top of the European political agenda. As right-wing parties have gained at the ballot box through their an… [+19441 chars]",
        "description": "Since 2016 the EU has intervened massively into African affairs in order to prevent further migration. But has it been effective, and how have Africans perceived this onslaught?",
        "publishedAt": "2020-05-17T00:00:00Z",
        "source": {
            "id": null,
            "name": "Open Democracy"
        },
        "title": "After the 'migration crisis': how Europe works to keep Africans in Africa",
        "url": "https://www.opendemocracy.net/en/beyond-trafficking-and-slavery/after-migration-crisis-how-europe-works-keep-africans-africa/",
        "urlToImage": "https://cdn-prod.opendemocracy.net/media/images/Cover_Colour_crop.2e16d0ba.fill-1200x630.jpg"
    },
    {
        "author": "communities@mercola.com (Dr. Joseph Mercola)",
        "content": "Disclaimer: The entire contents of this website are based upon the opinions of Dr. Mercola, unless otherwise noted. Individual articles are based upon the opinions of the respective author, who retai… [+1049 chars]",
        "description": "\"In a room where people unanimously maintain a conspiracy of silence, one word of truth sounds like a pistol shot.\" ~ Czesław Miłosz1\r\n\n\nIn recent years, a number of brave individuals have alerted us to the fact that we're all being monitored and manipulated …",
        "publishedAt": "2020-05-17T00:00:00Z",
        "source": {
            "id": null,
            "name": "Mercola.com"
        },
        "title": "Harvard Professor Exposes Google and Facebook",
        "url": "https://articles.mercola.com/sites/articles/archive/2020/05/17/surveillance-capitalism.aspx",
        "urlToImage": "https://media.mercola.com/ImageServer/Public/2020/March/FB/surveillance-capitalism-fb.jpg"
    },
    {
        "author": "Scott Morefield",
        "content": "YouTube removed a video of a prominent epidemiologist explaining his view that achieving “herd immunity” is the best way to combat the ongoing coronavirus pandemic.\r\nDr. Knut M. Wittkowski is a forme… [+2562 chars]",
        "description": "YouTube removed a video of a prominent epidemiologist explaining his view that achieving \"herd immunity\" is the best way to combat the coronavirus pandemic.",
        "publishedAt": "2020-05-16T23:59:21Z",
        "source": {
            "id": null,
            "name": "The Daily Caller"
        },
        "title": "Epidemiologist’s Video On Coronavirus ‘Herd Immunity’ Had 1.3 Million Views, Until YouTube Removed It",
        "url": "https://dailycaller.com/2020/05/16/knut-wittkowski-youtube-censorship-coronavirus-herd-immunity/",
        "urlToImage": "https://cdn01.dailycaller.com/wp-content/uploads/2020/05/GettyImages-936980924-e1589667713637.jpg"
    },
    {
        "author": "Lara Pearce",
        "content": "Coupons: Shop and save with our best Tech deals of 2020",
        "description": "<p>A nine-year-old boy in France has died from symptoms similar to those of Kawasaki disease after testing positive to COVID-19.</p>",
        "publishedAt": "2020-05-16T23:57:43Z",
        "source": {
            "id": null,
            "name": "9News"
        },
        "title": "Coronavirus: Boy, 9, dies from Kawasaki-like illness in French hospital",
        "url": "https://www.9news.com.au/national/coronavirus-boy-9-dies-from-kawasaki-like-illness-in-french-hospital/9a306eb6-43ed-40c1-9747-e2bc90c7500e",
        "urlToImage": "https://imageresizer.static9.net.au/hEuMtDXNx1m8GWDt7tF8CisfSAg=/1200x628/smart/https%3A%2F%2Fprod.static9.net.au%2Ffs%2F6ed93802-9729-4e2c-b9c8-bf6a3f362f59"
    }
]

## Getting Top News Articles About NASA Picture of the Day

Takes date as input and returns the top news article about the NASA picture of the day between specified date and today.

### URL: "/api/news/nasa
### Method: GET
### Parameters:/{{date}}

### Response:
#### URL:http://127.0.0.1:5000/api/news/2020-05-13


{
    "author": "Shannon Stirone",
    "content": "Jupiter has one of the most bizarre atmospheres in the entire solar system. Gas giants like Jupiter are believed to have some kind of semi-solid core, but are mostly made of gas like hydrogen, helium… [+3273 chars]",
    "description": "NASA's Juno orbiter, along with its Hubble and Gemini telescopes, will help scientists better understand the planet's atmosphere.",
    "publishedAt": "2020-05-23T14:00:00Z",
    "source": {
        "id": "wired",
        "name": "Wired"
    },
    "title": "Space Photos of the Week: Keeping an Eye on Jupiter's Storms",
    "url": "https://www.wired.com/story/space-photos-keeping-an-eye-on-jupiters-storms/",
    "urlToImage": "https://media.wired.com/photos/5ec85271448999d7ae47db3f/191:100/w_1280,c_limit/photo_space_juno_2_PIA21972.jpg"
}


## Getting Currency Rates for Date

Takes date as input and returns the currency rates for specific date.

### URL: "/api/currencies/
### Method: GET
### Parameters:/{{date}}

### Response:
#### URL:http://127.0.0.1:5000/api/currencies/2020-05-13

{
"base": "TRY",
"date": "2020-05-13",
"rates": {
"CAD": 0.2009332859,
"EUR": 0.1318200393,
"GBP": 0.1163245937,
"USD": 0.1433542927
}
}

