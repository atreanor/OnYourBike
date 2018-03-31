# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')
import datetime
from time import sleep
from Application_Server import JCDecaux
from Application_Server import databaser
from Application_Server import owm

#from tests import test_basic

import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input):
    """Console script for led_tester."""

    print("Welcome to OnYourBike's Application Server!!! :)")

    # Initalize the Bike_scraper class:
    x = JCDecaux.JCDecaux_scrape_init()
    # Initalize the open weather map scraper class:
    y = owm.owm_connect()

    # Call the MYSQL database connection function:
    #databaser.connector()
    # Request current weather data:
    owm_current = y.owm_request_current()

    #Parse current weather response (JSON):
    y.owm_parse_current(owm_current)

    # Call function to execute insert function every half hour:
    y.insert_scheduler()

    # Static data - Call the method to scrape Dublin data and return json
    print("JCDecaux - Request static data")
    #static_data = x.scrape_jcdecaux()

    # Call parse_json method to parse the json response
    for i in static_data:
        number, contract_name, name, address, lat, lng, banking, bonus = x.parse_json(i)
        # Call method to add static information to database
        databaser.inserter_static(number, contract_name, name, address, lat, lng, banking, bonus)

    # The scheduler schedules scraping of dynamic data from JCDecaux
    def scheduler():
        while True:
            try:
                print("Request Dynamic data - Executed by scheduler:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
                dynamic_json = x.scrape_jcdecaux()
                x.parse_dynamic(dynamic_json)
                sleep(300)

            except NameError as e:
                print(__name__, "-", e)
                sleep(10)
                exit()

            except KeyboardInterrupt as e:
                print("\n You have stopped the scheduler \n Goodbye!")
                exit()

            #except Exception as ex:
            #    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            #    message = template.format(type(ex).__name__, ex.args)
            #    print(message)
            #    print(ex)
            #    exit()
    return 0

    scheduler()

    return 0


if __name__ == "__main__":
    sys.exit(main())
