import requests
import json
import databaser
from databaser import *
import sys
import core
import datetime
#import db
 # This will always return the same object
sys.path.append('.')


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
        print("Scrape response status:", response.status_code)
        #print(json_response)
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
        return number, contract_name, name, address, lat, lng, banking, bonus

# start=0
#  
# for start to lenght of dynamic json
#  
# at end - increment start by lenght of dynamic json


    def parse_dynamic(self, dynamic_json):
        print("length of dynamic json is ", len(dynamic_json))
        counter=0
        for i in dynamic_json:
            print(i)
            number = (i['number'])
            status = (i['status'])
            bike_stands = (i['bike_stands'])
            available_bike_stands = (i['available_bike_stands'])
            available_bikes = (i['available_bikes'])
            last_update = (i['last_update'])
            lu_sec = last_update/1000
            lu_dt = datetime.datetime.fromtimestamp(lu_sec)
            print(number, status, bike_stands, available_bike_stands, available_bikes, lu_dt)
            inserter_dynamic(number, status, bike_stands, available_bike_stands, available_bikes, lu_dt)
            counter = counter+1
            print("counter is ", counter)
        return 0

    