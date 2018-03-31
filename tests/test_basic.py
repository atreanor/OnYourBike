import unittest
import sys

sys.path.append('.')

from Application_Server.scraper import Bike_scraper


class TestBasicFunction(unittest.TestCase):

    def test_scraper_constructor(self):
        uut = Bike_scraper('mockContract', 'mockKey')
        assert uut.contract == 'mockContract'
        assert uut.apikey == 'mockKey'


    def test_scrape_static(self):
        uut = Bike_scraper('Dublin', 'e8823ad03eaa6b4b5b80b84203e56c1740394008')
        returned = uut.scrape_static()
        self.assertTrue(isinstance(returned, list))


    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        self.assertTrue(True)

    def test_3(self):
        pass


if __name__ == '__main__':
    unittest.main()
