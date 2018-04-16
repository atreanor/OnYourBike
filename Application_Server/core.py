# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')

from Application_Server import JCDecaux
from Application_Server import databaser
from Application_Server import owm
#from tests import test_basic

print("Welcome to OnYourBike's Application Server!!!")

def bikes_static():
    print("JCDecaux Static Scheduler:")
    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the Bike_scraper class:
    static = JCDecaux.JCDecaux_scrape_init()

    #start the static scheduler:
    static.jcd_s_scheduler()

def bikes_dynamic():
    print("JCDecaux Dynamic Scheduler:")
    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the Bike_scraper class:
    dynamic = JCDecaux.JCDecaux_scrape_init()
    # Start the dynamic scheduler:
    dynamic.jcd_d_scheduler()

def weather():

    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the open weather map scraper class:
    y = owm.owm_connect()
    y.owm_scheduler()


def testweather():

    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the open weather map scraper class:
    y = owm.owm_connect()
    y.owm_request_current()
    y.owm_parse_current()

    print(y.name, y.visibility, y.w_d_main, y.w_id, y.w_icon, y.w_description, y.owm_dt)

if __name__ == "__main__":
    sys.exit(bikes_static())
