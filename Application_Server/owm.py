# -*- coding: utf-8 -*-
import requests
import json
import sys
import datetime
from time import sleep
from Application_Server import databaser

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

    def __init__(self, owm_key, owm_city, owm_country):
        # Variables to store OWM connection data:
        self._owm_key = owm_key
        self._owm_city = owm_city
        self._owm_country = owm_country
        # JSON:
        self.owm_json = None
        # Weather visibility:
        self.clouds = None
        self.name = None
        self.visibility = None
        # General weather description:
        self.w_d_main = None
        self.w_Drizzle = None
        self.w_d_id = None
        self.w_d_icon = None
        self.w_description = None
        # Location info
        self.cod = None
        self.coord_lat = None
        self.coord_long = None
        self.owm_dt = None
        self.id = None
        # Temperature info
        self.humidity = None
        self.pressure = None
        self.temp = None
        self.temp_min = None
        self.temp_max = None
        self.city = None
        # Wind:
        self.wind_speed = None
        self.wind_deg = None

        # System info:
        self.sys_country = None
        self.sys_id = None
        self.sys_message = None
        self.sys_sunrise_dt = None
        self.sys_sunset_dt = None
        self.sys_type = None

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
                  + ","+self._owm_country+"&appid="+self._owm_key+"&units=metric"
        response = requests.get(api_url)
        self.owm_json = json.loads(response.content)
        print("Response received from Open Weather Map:", response.status_code)
        return None

    def owm_parse_current(self):
        self.clouds = self.owm_json['clouds'][('all')]
        self.name = self.owm_json['name']
        self.visibility = self.owm_json['visibility']
        # Parse general weather description:
        self.w_d_main = self.owm_json['weather'][0]['main']
        self.w_d_id = self.owm_json['weather'][0]['id']
        self.w_d_icon = self.owm_json['weather'][0]['icon']
        self.w_description = self.owm_json['weather'][0]['description']
        # Location info:
        self.cod = self.owm_json['cod']
        self.coord_lat = self.owm_json['coord']['lat']
        self.coord_long = self.owm_json['coord']['lon']
        self.owm_dt = datetime.datetime.fromtimestamp(self.owm_json['dt'])
        self.id = self.owm_json['id']
        # Temperature info
        self.humidity = self.owm_json['main']['humidity']
        self.pressure = self.owm_json['main']['pressure']
        self.temp = self.owm_json['main']['temp']
        self.temp_min = self.owm_json['main']['temp_min']
        self.temp_max = self.owm_json['main']['temp_max']
        self.city = self.owm_json['name']
        self.sys_country = self.owm_json['sys']['country']
        self.sys_id = self.owm_json['sys']['id']
        self.sys_message = self.owm_json['sys']['message']
        self.sys_sunrise_dt = datetime.datetime.fromtimestamp(self.owm_json['sys']['sunrise'])
        self.sys_sunset_dt = datetime.datetime.fromtimestamp(self.owm_json['sys']['sunset'])
        self.sys_type = self.owm_json['sys']['type']

        return 0

    def owm_scheduler(self):
        while True:
            try:
                sleep(10)
                self.owm_request_current()
                # Sleep 5 is required to not accidentally violate OWM T&C
                sleep(10)
                self.owm_parse_current()
                print("Parsed!")
                databaser.insert_owm_current(self.clouds, self.name, self.visibility, self.w_d_main, self.w_d_id, self.w_d_icon, self.w_description, self.coord_lat, self.coord_long, self.owm_dt, self.id, self.humidity, self.pressure, self.temp, self.temp_min, self.temp_max, self.city, self.sys_country, self.sys_id, self.sys_message, self.sys_sunrise_dt, self.sys_sunset_dt, self.cod)

                # Execute every 0.5 hours  (1800 seconds)
                sleep(1800)

            except Exception as e:
                logf.write(str(e))
                print("Exception: ", e)
            pass

        return None



