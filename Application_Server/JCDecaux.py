# -*- coding: utf-8 -*-
import requests
import json
from Application_Server import databaser
import sys
from time import sleep

import datetime

 # This will always return the same object
sys.path.append('.')

#Open a log file:
logf = open("JCDecaux.log", "w")

# This function initializes the Bike_scraper class:

def JCDecaux_scrape_init ():
    contract = "Dublin"
    apikey = "e8823ad03eaa6b4b5b80b84203e56c1740394008" # API key for JC Decaux
    return Bike_scraper(contract, apikey)

class Bike_scraper:
    json_response = None

    def __init__(self, contract, apikey):
        self.contract = contract
        self.apikey = apikey
        # class variables for static weather:
        self.number = None
        self.s_contract_name = None
        self.s_name = None
        self.s_address = None
        self.s_lat = None
        self.s_lng = None
        self.s_banking = None
        self.s_bonus = None
        # variables for dynamic weather:
        self.d_status = None
        self.d_bike_stands = None
        self.d_bike_stands = None
        self.d_available_bike_stands = None
        self.d_available_bikes = None
        self.d_last_update = None

    def scrape_jcdecaux(self):
        contract = self.contract
        api_url = "https://api.jcdecaux.com/vls/v1/stations?contract="+self.contract+"&apiKey="+self.apikey+""
        response = requests.get(api_url)
        json_response = json.loads(response.content)
        print("JCD response:", response.status_code)
        return json_response

    def parse_flask(self, json_response):

        print("Length of dynamic json is ", len(json_response))
        for i in json_response:
            # Static variables
            self.number = (i['number'])
            self.s_contract_name = (i['contract_name'])
            self.s_name = (i['name'])
            self.s_address = (i['address'])
            self.s_lat = i['position']['lat']
            self.s_lng = i['position']['lng']
            self.s_banking = (i['banking'])
            self.s_bonus = (i['bonus'])
            self.d_status = (i['status'])
            self.d_bike_stands = (i['bike_stands'])
            self.d_available_bike_stands = (i['available_bike_stands'])
            self.d_available_bikes = (i['available_bikes'])
            self.d_last_update = datetime.datetime.fromtimestamp((i['last_update']) / 1000)

            # Execute insert function:
            self.execute_flask_insert()
        return 0

    def execute_flask_insert(self):
        databaser.insert_jdc_flask(self.number, self.s_name, self.s_contract_name, self.d_status, self.d_bike_stands, self.d_available_bike_stands, self.d_available_bikes, self.d_last_update, self.s_address, self.s_lat, self.s_lng, self.s_banking, self.s_bonus)

        return 0

    def parse_dynamic(self, json_response):
        for i in json_response:
            # Static variables
            self.number = (i['number'])
            self.d_status = (i['status'])
            self.d_bike_stands = (i['bike_stands'])
            self.d_available_bike_stands = (i['available_bike_stands'])
            self.d_available_bikes = (i['available_bikes'])
            self.d_last_update = (i['last_update'])
            lu_sec = self.d_last_update / 1000
            lu_dt = datetime.datetime.fromtimestamp(lu_sec)
            # print(number, status, bike_stands, available_bike_stands, available_bikes, lu_dt)
            databaser.inserter_dynamic(self.number, self.d_status, self.d_bike_stands, self.d_available_bike_stands, self.d_available_bikes, lu_dt)
        print("Dynamic data - Parsed and SQL executed")

        return 0

    def jcd_d_scheduler(self):
        print("JCDecaux Dynamic Scheduler:")

        while True:
            try:
                print("JCD Dynamic scheduler:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
                json_response = self.scrape_jcdecaux()
                sleep(5)
                self.parse_dynamic(json_response)
                # Execute every 1 hour  (300 seconds)
                sleep(3600)

            except Exception as e:
                logf.write(str(e))
                pass

        return 0

    def jcd_flask_scheduler(self):

        while True:
            try:
                print("JCD Flask scheduler:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
                json_response = self.scrape_jcdecaux()
                sleep(5)
                databaser.truncate_JCD_Flask_table()
                sleep(5)
                self.parse_flask(json_response)
                # Execute every 5 minutes  (300 seconds)
                sleep(300)

            except Exception as e:
                logf.write(str(e))
                pass

            return 0
