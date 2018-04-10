# -*- coding: utf-8 -*-
import requests
import json
import sys
import datetime
from time import sleep
from Application_Server import databaser
import pprint

# This will always return the same object
sys.path.append('.')

# Open a log file:
logf = open("OWM.log", "w")

# This function initializes the owm_scrape class:
def owm_connect():
    owm_key = "350d70da9c80ab41ceec02a84094004d" # API key for Open Weather Map
    owm_city = "Dublin"
    owm_country = "ie"
    return OpenWeatherMap(owm_key, owm_city, owm_country)


class OpenWeatherMap:
    parsed_json = None

    def __init__(self, owm_key, owm_city, owm_country):
        # Variables to store OWM connection data:
        self._owm_key = owm_key
        self._owm_city = owm_city
        self._owm_country = owm_country
        # variables to store weather data:
        self.clouds = None
        self.cod = None
        self.coord_lat = None
        self.coord_long = None
        self.owm_datetime = None
        self.id = None
        self.humidity = None
        self.pressure = None
        self.temp = None
        self.temp_min = None
        self.temp_max = None
        self.city = None
        self.country = None
        self.sys_id = None
        self.sys_message = None
        self.sunrise = None
        self.sunset = None
        self.sys_type = None
        self.date_dt = None
        self.sunrise_dt = None
        self.sunset_dt = None

    # Python Class Encapsulation - Properties (getter), setters
    @property
    def owm_key(self):
        return self._owm_key

    @property
    def owm_city(self):
        return self._owm_city

    @property
    def owm_country(self):
        return self._owm_country

    @owm_city.setter
    def owm_city(self, owm_city):
        self._owm_city = owm_city

    @owm_country.setter
    def owm_country(self, owm_country):
        self._owm_country = owm_country

    @owm_key.setter
    def owm_key(self, owm_key):
        self._owm_key = owm_key

    def owm_request_current(self):
        api_url = "http://api.openweathermap.org/data/2.5/weather?q="+self._owm_city+","\
                  +self._owm_country+"&appid="+self._owm_key
        response = requests.get(api_url)
        global owm_json
        owm_json = json.loads(response.content)
        print("Response received from Open Weather Map:", response.status_code)
        return None


    def owm_parse_current(self):
        self.clouds = owm_json['clouds']['all']
        self.cod = owm_json['cod']
        self.coord_lat = owm_json['coord']['lat']
        self.coord_long = owm_json['coord']['lon']
        self.owm_datetime = owm_json['dt']
        self.id = owm_json['id']
        self.humidity = owm_json['main']['humidity']
        self.pressure = owm_json['main']['pressure']
        self.temp = owm_json['main']['temp']
        self.temp_min = owm_json['main']['temp_min']
        self.temp_max = owm_json['main']['temp_max']
        self.city = owm_json['name']
        self.country = owm_json['sys']['country']
        self.sys_id = owm_json['sys']['id']
        self.sys_message = owm_json['sys']['message']
        self.sunrise = owm_json['sys']['sunrise']
        self.sunset = owm_json['sys']['sunset']
        self.sys_type = owm_json['sys']['type']
        self.date_dt = datetime.datetime.fromtimestamp(self.owm_datetime)
        self.sunrise_dt = datetime.datetime.fromtimestamp(self.sunrise)
        self.sunset_dt = datetime.datetime.fromtimestamp(self.sunset)
        print("Weather data received from OWM as of:", self.date_dt.strftime("%Y-%m-%d %H:%M"))
        return 0

    def owm_scheduler(self):
        while True:
            try:
                print("hello")
                self.owm_request_current()
                print("Will parse")
                self.owm_parse_current()
                print("Parsed!")
                print("Open Weather Map - Scheduler running every half an hour:")
                databaser.insert_owm_current(self.clouds, self.cod, self.coord_lat, self.coord_long, self.date_dt,
                                             self.id, self.humidity,self.pressure, self.temp, self.temp_min,
                                             self.temp_max, self.city, self.country, self.sys_id, self.sys_message,
                                             self.sunrise_dt, self.sunset_dt)
                # Execute every 0.5 hours  (1800 seconds)
                sleep(1800)

            except Exception as e:
                logf.write(str(e))
            pass

        return None



