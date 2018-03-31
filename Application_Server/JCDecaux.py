# -*- coding: utf-8 -*-
import requests
import json
from Application_Server import databaser
import sys

import datetime

 # This will always return the same object
sys.path.append('.')

# This function initializes the Bike_scraper class:

def JCDecaux_scrape_init ():
    contract = "Dublin"
    apikey = "e8823ad03eaa6b4b5b80b84203e56c1740394008" # API key for JC Decaux
    return Bike_scraper(contract, apikey)

class Bike_scraper:
    parsed_json = None

    def __init__(self, contract, apikey):
        self.contract = contract
        self.apikey = apikey
        return None

    def scrape_jcdecaux(self):
        contract = self.contract
        api_url = "https://api.jcdecaux.com/vls/v1/stations?contract="+self.contract+"&apiKey="+self.apikey+""
        response = requests.get(api_url)
        json_response = json.loads(response.content)
        print("Response received from JC Decaux:", response.status_code)
        return json_response

    def parse_json(self, i):
        #print('Entry : {}'.format(i))
        number = (i['number'])
        contract_name = (i['contract_name'])
        name = (i['name'])
        address = (i['address'])
        lat = i['position']['lat']
        lng = i['position']['lng']
        banking = (i['banking'])
        bonus = (i['bonus'])
        #print(number, contract_name, name, address, lat, lng, banking, bonus)
        #print("Static data parsed")
        return number, contract_name, name, address, lat, lng, banking, bonus

# start=0
#  
# for start to lenght of dynamic json
#  
# at end - increment start by lenght of dynamic json


    def parse_dynamic(self, dynamic_json):
        print("Length of dynamic json is ", len(dynamic_json))
        for i in dynamic_json:
            number = (i['number'])
            status = (i['status'])
            bike_stands = (i['bike_stands'])
            available_bike_stands = (i['available_bike_stands'])
            available_bikes = (i['available_bikes'])
            last_update = (i['last_update'])
            lu_sec = last_update/1000
            lu_dt = datetime.datetime.fromtimestamp(lu_sec)
            #print(number, status, bike_stands, available_bike_stands, available_bikes, lu_dt)
            databaser.inserter_dynamic(number, status, bike_stands, available_bike_stands, available_bikes, lu_dt)
        print("Dynamic data parsed and SQL insert statements executed")
        return 0