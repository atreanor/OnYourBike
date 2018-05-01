# -*- coding: utf-8 -*-
import requests
import json
import sys
import datetime

# This will always return the same object
sys.path.append('.')


class WeatherScrape:
    """ class to represent Open Weather Map API request & parsing of returned json object """

    parsed_json = None

    def __init__(self, key_owm, city, country):
        """ constructor initialises variables """

        self._key_owm = key_owm
        self._city = city
        self._country = country
        print(key_owm, city, country)

    # Python Class Encapsulation - Properties (getter), setters and delete
    @property
    def key_owm(self):
        """ method to return API key """

        return self._key_owm

    @property
    def city(self):
        """ method to return city """

        return self._city

    @property
    def country(self):
        """ method to return country """

        return self._country

    @city.setter
    def city(self, city):
        """ method to set city """

        self._city = city

    @country.setter
    def country(self, country):
        """ method to set country """

        self._country = country

    @key_owm.setter
    def key_owm(self, key_owm):
        """ method to set API key """
        self._key_owm = key_owm

    def owm_current(self):
        """ method to make API request & return json object """

        api_url = "http://api.openweathermap.org/data/2.5/weather?q="+self.city+","+self.country+"&appid="+self.key_owm
        response = requests.get(api_url)
        owm_json = json.loads(response.content)
        print("Response received from Open Weather Map:", response.status_code)

        return owm_json

    def owm_parse_current(self, owm_current):
        """ method to parse current Open Weather Map API json data """

        clouds = owm_current['clouds']['all']
        cod = owm_current['cod']
        coord_lat = owm_current['coord']['lat']
        coord_long = owm_current['coord']['lon']
        owm_datetime = owm_current['dt']
        humidity = owm_current['main']['humidity']
        pressure = owm_current['main']['pressure']
        temp = owm_current['main']['temp']
        temp_min = owm_current['main']['temp_min']
        temp_max = owm_current['main']['temp_max']
        city = owm_current['name']
        country = owm_current['sys']['country']
        sunrise = owm_current['sys']['sunrise']
        sunset = owm_current['sys']['sunset']

        date_dt = datetime.datetime.fromtimestamp(owm_datetime)
        print("Weather data as of:", date_dt.strftime("%Y-%m-%d %H:%M"))

        return clouds, cod, coord_lat, coord_long, date_dt, humidity, pressure, temp, temp_min, temp_max, city, \
               country, sunrise, sunset
