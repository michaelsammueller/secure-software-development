'''
    This file contains the Thermometer class.
'''
from classes.sensors.abstract import Sensor
from random import gauss


class Thermometer(Sensor):
    '''
        A class for encapsulating a thermometer component.
    '''
    def __init__(self):
        self._temperature = gauss(25.0, 5.0) # Random temperature
        self._unit = 'C'
        self._RATEOFCHANGE = 1

    def __repr__(self):
        return f'Thermometer({self._temperature} {self._unit})'

    def read_data(self, unit='C'):
        '''
            A method for reading data from the thermometer.
        '''
        # Random temperature variation
        delta = self.get_converters()[self._unit](gauss(0.0, 0.5 * self._RATEOFCHANGE), 'C')
        self._temperature = self.get_converters()[unit](self._temperature + delta, self._unit)
        self._unit = unit
        return self._temperature

    @classmethod
    def convert_to_celsius(cls, temperature, unit):
        '''
            A method for converting the temperature to Celsius.
        '''
        if unit == 'C':
            return temperature
        elif unit == 'F':
            return (temperature - 32) * 5/9
        elif unit == 'K':
            return temperature - 273.15
    
    @classmethod
    def convert_to_fahrenheit(cls, temperature, unit):
        '''
            A method for converting the temperature to Fahrenheit.
        '''
        if unit == 'C':
            return (temperature * 9/5) + 32
        elif unit == 'F':
            return temperature
        elif unit == 'K':
            return (temperature * 9/5) - 459.67
        
    @classmethod
    def convert_to_kelvin(cls, temperature, unit):
        '''
            A method for converting the temperature to Kelvin.
        '''
        if unit == 'C':
            return temperature + 273.15
        elif unit == 'F':
            return (temperature + 459.67) * 5/9
        elif unit == 'K':
            return temperature

    @classmethod
    def get_converters(cls):
        '''
            A method for getting conversion methods.
        '''
        func_map = {
            'C': cls.convert_to_celsius,
            'F': cls.convert_to_fahrenheit,
            'K': cls.convert_to_kelvin
        }
        return func_map