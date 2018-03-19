# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')
from tests import test_basic

import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input):
    """Console script for led_tester."""

    print("Input(path/URL):", input)
    # Process input to get n
    n, instructions = led_tester.processInput(input)
    # Initiate Light_board class to define light_board with n
    x = scraper.Bike_scraper(n)
    # Call the apply_instruction method for each set of instructions
    for instr in instructions:
        x.apply_instruction(instr)
    # Call the LB_statistics method to view light board statistics
    x.LB_statistics(n, instructions)
    return 0

if __name__ == "__main__":
    sys.exit(main())
