# -*- coding: utf-8 -*-
import requests
import json
import sys
import datetime

# This will always return the same object
sys.path.append('.')

class owm_scrape:
    parsed_json = None

    def __init__(self, key_owm, city, country):
        self._key_owm = key_owm
        self._city = city
        self._country = country
        print(key_owm, city, country)
        return None

    # Python Class Encapsulation - Properties (getter), setters and delete
    @property
    def key_owm(self):
        return self._key_owm

    @property
    def city(self):
        return self._city

    @property
    def country(self):
        return self._country

    @city.setter
    def city(self, city):
        self._city = city

    @country.setter
    def country(self, country):
        self._country = country

    @key_owm.setter
    def key_owm(self, key_owm):
        self._key_owm = key_owm

    def owm_current(self):
        api_url = "http://api.openweathermap.org/data/2.5/weather?q="+self.city+","+self.country+"&appid="+self.key_owm
        response = requests.get(api_url)
        owm_json = json.loads(response.content)
        print("Response received from Open Weather Map:", response.status_code)
        return owm_json

    def owm_parse_current(self, owm_current):
        clouds = owm_current['clouds']['all']
        cod = owm_current['cod']
        coord_lat = owm_current['coord']['lat']
        coord_long = owm_current['coord']['lon']
        owm_datetime = owm_current['dt']
        #id_1 = owm_current['id']
        humidity = owm_current['main']['humidity']
        pressure = owm_current['main']['pressure']
        temp = owm_current['main']['temp']
        temp_min = owm_current['main']['temp_min']
        temp_max = owm_current['main']['temp_max']
        city = owm_current['name']
        country = owm_current['sys']['country']
        #sys_id = owm_current['sys']['id']
        #sys_message = owm_current['sys']['message']
        sunrise = owm_current['sys']['sunrise']
        sunset = owm_current['sys']['sunset']
        #sys_type = owm_current['sys']['type']

        date_dt = datetime.datetime.fromtimestamp(owm_datetime)
        print("Weather data as of:", date_dt.strftime("%Y-%m-%d %H:%M"))

        #print(clouds, cod, coord_lat, coord_long, date_dt, id_1, humidity, pressure, temp, temp_min, temp_max, city, country, sys_id, sys_message, sunrise, sunset, sys_type)
        return clouds, cod, coord_lat, coord_long, date_dt, humidity, pressure, temp, temp_min, temp_max, city, country, sunrise, sunset

