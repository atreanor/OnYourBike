# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')

from Application_Server import JCDecaux
from Application_Server import databaser
from Application_Server import owm
#from tests import test_basic

print("Welcome to OnYourBike's Application Server!!!")


def bikes_flask():
    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the Bike_scraper class:
    jcd_flask = JCDecaux.JCDecaux_scrape_init()
    #start the jdc_flask_scheduler:
    jcd_flask.jcd_flask_scheduler()


def bikes_dynamic():
    print("JCDecaux Dynamic Table Scheduler:")
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

if __name__ == "__main__":
    sys.exit(bikes_dynamic())
