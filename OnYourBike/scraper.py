import pprint
import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

import sys
sys.path.append('.')

class Bike_scraper:

    def __init__(self, contract, apikey):
        self.contract = contract
        self.apikey = apikey
        self.__main__(contract)

    def __main__(self, contract):
        self.scrape_static()
        print("scrape_static method called")
        scheduler = BlockingScheduler()
        scheduler.add_job(self.scrape_dynamic, 'interval', seconds=10)
        scheduler.start()
        return 0

    def scrape_static(self):
        contract = self.contract
        api_url = "https://api.jcdecaux.com/vls/v1/stations?contract="+self.contract+"&apiKey="+self.apikey+""
        response = requests.get(api_url)
        parsed_json = json.loads(response.content)
        '''
        #save to a file:
        with open('data.txt', 'w') as outfile:
            json.dump(parsed_json, outfile)
        '''
        count = 0
        for i in parsed_json:
            number = (i['number'])
            contract_name = (i['contract_name'])
            name = (i['name'])
            address = (i['address'])
            lat = i['position']['lat']
            lng = i['position']['lng']
            banking = (i['banking'])
            bonus = (i['bonus'])
            count +=1
            #print(count,number, contract_name, name, address, lat, lng, banking, bonus)

        print("Scheduler called scrape_static method,", "Response status code:", response.status_code, ", Time:", datetime.datetime.now())

    def scrape_dynamic(self):
        contract = self.contract
        api_url = "https://api.jcdecaux.com/vls/v1/stations?contract="+self.contract+"&apiKey="+self.apikey+""
        response = requests.get(api_url)
        #print(response.status_code)
        parsed_json = json.loads(response.content)
        '''
        #save to a file:
        with open('data.txt', 'w') as outfile:
            json.dump(parsed_json, outfile)
        '''
        count = 0
        for i in parsed_json:
            number = (i['number'])
            status = (i['status'])
            bike_stands = (i['bike_stands'])
            available_bike_stands = (i['available_bike_stands'])
            available_bikes = (i['available_bikes'])
            last_update = (i['last_update'])
            count +=1
            lu_seconds = last_update / 1000
            dt_obj = datetime.datetime.fromtimestamp(lu_seconds)
            #print(count,number, status, bike_stands, available_bike_stands, available_bikes, dt_obj)
        print("Scheduler called scrape_dynamic method,", "Response status code:", response.status_code, datetime.datetime.now())

        #pprint.pprint(parsed_json)
        #print(len(parsed_json))
        #print(response.url)
        return 0