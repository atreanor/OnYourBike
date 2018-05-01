# -*- coding: utf-8 -*-
from Application_Server import JCDecaux
from Application_Server import databaser
from Application_Server import owm

import sys
sys.path.append('.')


print("Welcome to OnYourBike's Application Server!!!")


def bikes_flask():
    """ method to invoke flask database connection """

    # Call the MYSQL database connection function
    databaser.connector()
    # Initalize the Bike_scraper class:
    jcd_flask = JCDecaux.jc_decaux_scrape_init()
    # start the jdc_flask_scheduler:
    jcd_flask.jcd_flask_scheduler()


def bikes_dynamic():
    """ method to invoke dynamic database connection """

    print("JCDecaux Dynamic Table Scheduler:")
    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the Bike_scraper class:
    dynamic = JCDecaux.jc_decaux_scrape_init()
    # Start the dynamic scheduler:
    dynamic.jcd_d_scheduler()


def weather():
    """ method to invoke open weather map database connection """

    # Call the MYSQL database connection function:
    databaser.connector()
    # Initalize the open weather map scraper class:
    y = owm.owm_connect()
    y.owm_scheduler()


if __name__ == "__main__":
    sys.exit(bikes_dynamic())
