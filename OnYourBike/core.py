# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')
from OnYourBike import scraper
#from tests import test_basic

import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input):
    """Console script for led_tester."""

    print("Input(path/URL):", input)
    # Process input to get n

    contract = "Dublin"
    apikey = "e8823ad03eaa6b4b5b80b84203e56c1740394008"
    # Initiate Light_board class to define light_board with n
    x = scraper.Bike_scraper(contract, apikey)

    # Call the LB_statistics method to view light board statistics
    #x.scrape(contract)
    return 0

if __name__ == "__main__":
    sys.exit(main())
