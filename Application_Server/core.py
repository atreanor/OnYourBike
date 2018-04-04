# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')

from Application_Server import JCDecaux
from Application_Server import databaser
from Application_Server import owm
from multiprocessing import Process
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
    databaser.connector()

    # JCDecaux Static data - Request, parse and execute SQL
    json_response = x.scrape_jcdecaux()
    x.parse_static(json_response)

    def func1():
        x.jcd_scheduler()

    def func2():
        y.owm_scheduler()

    return 0


if __name__ == "__main__":
    main()
    p1 = Process(target=main.func1)
    p1.start()
    p2 = Process(target=main.func2)
    p2.start()
