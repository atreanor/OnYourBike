import requests
import json

import sys
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

    def parse_dynamic(self, dynamic_json):
        for i in dynamic_json:
            number = (i['number'])
            status = (i['status'])
            bike_stands = (i['bike_stands'])
            available_bike_stands = (i['available_bike_stands'])
            available_bikes = (i['available_bikes'])
            last_update = (i['last_update'])
            # dbobj1.inserter_dynamic(number, status, bike_stands, available_bike_stands, available_bikes, last_update)
        return 0

        #pprint.pprint(parsed_json)
        #print(len(parsed_json))
        #print(response.url)
        return 0