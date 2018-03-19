import pprint
import re
import requests
import sys
sys.path.append('.')

class Bike_scraper:

    def __init__(self, n):
        self.lbSize = n
        self.light_board = [[0]*n for _ in range(n)]

    def LB_statistics(self, n, instructions):
        number_off = sum(i.count(0) for i in self.light_board)
        number_on = sum(i.count(1) for i in self.light_board)
        print("Number of instructions: {:0,.0f}".format(len(instructions)))
        print("Size of light board: {:0,.0f}".format(n), "rows, {:0,.0f}".format(n), "columns", "and {:0,.0f}".format(n*n), "light bulbs")
        print("Lights on: {:0,.0f}".format(number_on))
        print("Lights off: {:0,.0f}".format(number_off))
        print("Sum of on and off: {:0,.0f}".format(number_on + number_off))
        return 0