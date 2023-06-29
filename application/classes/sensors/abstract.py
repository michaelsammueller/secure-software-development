'''
    This file contains the abstract class for the sensors.
'''
from abc import ABC, abstractmethod


class Sensor(ABC):
    '''
        Abstract class for sensor components, 
        encapsulating hardware whose function is to provide 
        data to the system. 
    '''
    @abstractmethod
    def read_data():
        '''
            Abstract method for reading data from the sensor.
        '''