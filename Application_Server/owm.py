# -*- coding: utf-8 -*-
import requests
import json
import sys
import datetime
from time import sleep
from Application_Server import databaser

# This will always return the same object
sys.path.append('.')


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

    # Python Class Encapsulation - Properties (getter), setters and delete
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
        owm_json = json.loads(response.content)
        print("Response received from Open Weather Map:", response.status_code)
        return owm_json

    def owm_parse_current(self, owm_current):
        self.clouds = owm_current['clouds']['all']
        self.cod = owm_current['cod']
        self.coord_lat = owm_current['coord']['lat']
        self.coord_long = owm_current['coord']['lon']
        self.owm_datetime = owm_current['dt']
        self.id = owm_current['id']
        self.humidity = owm_current['main']['humidity']
        self.pressure = owm_current['main']['pressure']
        self.temp = owm_current['main']['temp']
        self.temp_min = owm_current['main']['temp_min']
        self.temp_max = owm_current['main']['temp_max']
        self.city = owm_current['name']
        self.country = owm_current['sys']['country']
        self.sys_id = owm_current['sys']['id']
        self.sys_message = owm_current['sys']['message']
        self.sunrise = owm_current['sys']['sunrise']
        self.sunset = owm_current['sys']['sunset']
        self.sys_type = owm_current['sys']['type']

        global date_dt
        global sunrise_dt
        global sunset_dt
        date_dt = datetime.datetime.fromtimestamp(self.owm_datetime)
        sunrise_dt = datetime.datetime.fromtimestamp(self.sunrise)
        sunset_dt = datetime.datetime.fromtimestamp(self.sunset)

        print("Weather data received from OWM as of:", date_dt.strftime("%Y-%m-%d %H:%M"))
        return date_dt, sunrise_dt, sunset_dt

    def insert_scheduler(self):
        while True:
            try:
                print("Open Weather Map - Insert Query executed:")
                databaser.insert_owm_current(self.clouds, self.cod, self.coord_lat, self.coord_long, date_dt,
                                             self.id, self.humidity,self.pressure, self.temp, self.temp_min,
                                             self.temp_max, self.city, self.country, self.sys_id, self.sys_message,
                                             sunrise_dt, sunset_dt)
                sleep(3600)

            except NameError as e:
                print(__name__, "-", e)
                sleep(10)
                exit()

            except KeyboardInterrupt as e:
                print("\n You have stopped the scheduler \n Goodbye!")
                exit()

        return None



