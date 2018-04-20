import sys

import test_db
import unittest


sys.path.append(".")
sys.path.append("../Application_Server/")
sys.path.append("../OYB_WebServer/")

#sys.path.append('Application_Server')

from JCDecaux import *
from app import views

class TestFunction(unittest.TestCase):

    def test_JCDecaux_scrape_init(self):
        # to test if bike scraper object is being created
        a = Bike_scraper('Dublin', 'e8823ad03eaa6b4b5b80b84203e56c1740394008')
        self.assertTrue(a.contract == 'Dublin')
        self.assertTrue(a.apikey == 'e8823ad03eaa6b4b5b80b84203e56c1740394008')
        self.assertTrue(isinstance(a, Bike_scraper))
        
    def test_scrape_jcdecaux(self):
        a = Bike_scraper('Dublin', 'e8823ad03eaa6b4b5b80b84203e56c1740394008')
        response = a.scrape_jcdecaux()
        print(response)
        self.assertTrue(response[0]['number']==42)    
        
    def test_connect_to_database(self):
        db = views.get_db()
        print(type(engine))
        result = getStations()
        print(result)
        
        

        

        