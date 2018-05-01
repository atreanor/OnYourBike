import unittest
import sys
from Application_Server import databaser
import MySQLdb

sys.path.append('.')

from Application_Server.JCDecaux import BikeScraper


class TestFunction(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(1==1)
    
    def test_scrape_jcdecaux(self):
        self.assertTrue(contract=="Dublin")
        self.assertTrue(contract=="e8823ad03eaa6b4b5b80b84203e56c1740394008")
    
    
    
    