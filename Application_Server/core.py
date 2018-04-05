# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')

from Application_Server import JCDecaux
from Application_Server import databaser
from Application_Server import owm
#from tests import test_basic

print(input, "Welcome to OnYourBike's Application Server!!!")

def bikes():

    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the Bike_scraper class:
    x = JCDecaux.JCDecaux_scrape_init()

    # JCDecaux Static data - Request, parse and execute SQL
    json_response = x.scrape_jcdecaux()
    x.parse_static(json_response)

    x.jcd_scheduler()

def weather():

    # Call the MYSQL database connection function:
    databaser.connector()

    # Initalize the open weather map scraper class:
    y = owm.owm_connect()

    y.owm_scheduler()

if __name__ == "__main__":
    sys.exit(weather())
