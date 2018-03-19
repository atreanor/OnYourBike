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
        print("main method automatically called")
        scheduler = BlockingScheduler()
        scheduler.add_job(self.scrape, 'interval', seconds=10)
        scheduler.start()
        return 0

    def scrape(self):
        contract = self.contract
        api_url = "https://api.jcdecaux.com/vls/v1/stations?contract="+self.contract+"&apiKey="+self.apikey+""
        response = requests.get(api_url)
        print(response.status_code)
        parsed_json = json.loads(response.content)
        '''
        #save to a file:
        with open('data.txt', 'w') as outfile:
            json.dump(parsed_json, outfile)
        '''
        count = 0
        for i in parsed_json:
            number = (i['number'])
            name = (i['name'])
            address = (i['address'])
            status = (i['status'])
            lat = i['position']['lat']
            lng = i['position']['lng']
            count +=1
            #print(count,number, name, address, status, lat, lng)
        print("Scheduler called scrape method", datetime.datetime.now())

        #pprint.pprint(parsed_json)
        #print(len(parsed_json))
        #print(response.url)
        return 0