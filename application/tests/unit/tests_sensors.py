'''
    This file contains unit tests for Sensor components.
'''
from context import GeigerCounter, Thermometer
import unittest

class TestGeigerCounter(unittest.TestCase):
    '''
        A class for encapsulating unit tests for a GeigerCounter.
    '''
    def setUp(self):
        self.geiger_counter = GeigerCounter()

    def test_read_data(self):
        '''
            A method that tests the read_data method.
        '''
        self.assertTrue(type(self.geiger_counter.read_data()) == float)

class TestThermometer(unittest.TestCase):
    '''
        A class for encapsulating unit tests for a GeigerCounter.
    '''
    def setUp(self):
        self.thermometer = Thermometer()

    def test_read_data(self):
        '''
            A method that tests the read_data method.
        '''
        self.assertTrue(type(self.thermometer.read_data()) == float)

if __name__ == '__main__':
    unittest.main()

