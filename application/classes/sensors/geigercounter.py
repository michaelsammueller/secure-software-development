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
        self._radiation = abs(gauss(0, 0.0005)) # Random radiation level
        self._unit = 'Rem'
        self._RATEOFCHANGE = 1

    def __repr__(self):
        return f'GeigerCounter({self._radiation} {self._unit})'

    def read_data(self, unit='Rem'):
        '''
            A method for reading data from the geiger counter.
        '''
        # Random radiation level variation
        delta = self.get_converters()[self._unit](gauss(0, 0.00001 * self._RATEOFCHANGE), 'Rem')
        self._radiation = max(self.get_converters()[unit](self._radiation + delta, self._unit), 0)
        self._unit = unit
        return self._radiation
    
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

   