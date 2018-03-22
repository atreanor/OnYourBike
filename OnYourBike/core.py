# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
from time import sleep
sys.path.append('.')

#Import files for classes
from OnYourBike import scraper
#from OnYourBike import databaser
#from tests import test_basic

import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input):
    """Console script for led_tester."""
    print("Welcome to OnYourBike")
    #print("Input(path/URL):", input)


    contract = "Dublin"
    apikey = "e8823ad03eaa6b4b5b80b84203e56c1740394008"
    # Initiate Light_board class to define light_board with n
    print("Scrape static")
    x = scraper.Bike_scraper(contract, apikey)
    # Static data - Call the method to scrape Dublin data and return json
    static_data = x.scrape_jcdecaux()
    # Create object of Databaser class so that parsed information can be added to the database
    # dbobj = Databaser()

    # Call parse_json method to parse the json response
    for i in static_data:
        number, contract_name, name, address, lat, lng, banking, bonus = x.parse_json(i)
        # Call method to add static information to database
        # dbobj.inserter_static(number, contract_name, name, address, lat, lng, banking, bonus)

    # The scheduler schedules scraping of dynamic data from JCDecaux
    def scheduler():
        while True:
            try:
                print("Scrape dynamic")
                dynamic_json = x.scrape_jcdecaux()
                x.parse_dynamic(dynamic_json)
                sleep(5)

            except NameError as e:
                print("Name error")
                print(e)
                sleep(300)
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
    #
    scheduler()

    return 0


if __name__ == "__main__":
    sys.exit(main())
