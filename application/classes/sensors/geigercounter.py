'''
    This file contains the GeigerCounter class.
'''
from classes.sensors.abstract import Sensor
from random import gauss


class GeigerCounter(Sensor):
    '''
        A class for encapsulating a geiger counter component.
    '''
    def __init__(self):
        self.__radiation = abs(gauss(0, 0.0005))  # Random radiation level
        self.__unit = 'Rem'
        self.__RATEOFCHANGE = 1

    def __repr__(self):
        return f'GeigerCounter({self.__radiation} {self.__unit})'

    def read_data(self, unit='Rem'):
        '''
            A method for reading data from the geiger counter.
        '''
        # Random radiation level variation
        delta = gauss(0, 0.00001 * self.__RATEOFCHANGE)
        self.__radiation_rem = max(self.get_converters()['Rem'](self.__radiation, self.__unit), 0)
        self.__radiation = max(self.get_converters()[unit](self.__radiation_rem + delta, 'Rem'), 0)
        self.__unit = unit
        return self.__radiation

    def get_units(self):
        '''
            A method for getting the units used for the last reading.
        '''
        return self.__unit

    @classmethod
    def convert_to_rem(cls, radiation, unit):
        '''
            A method for converting the radiation level to Rem.
        '''
        if unit == 'Rem':
            return radiation
        elif unit == 'SV':
            return radiation * 100

    @classmethod
    def convert_to_sievert(cls, radiation, unit):
        '''
            A method for converting the radiation level to Sievert.
        '''
        if unit == 'Rem':
            return radiation * 0.01
        elif unit == 'SV':
            return radiation

    @classmethod
    def get_converters(cls):
        '''
            A method for getting conversion methods.
        '''
        func_map = {
            'Rem': cls.convert_to_rem,
            'SV': cls.convert_to_sievert
        }
        return func_map
