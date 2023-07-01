'''
    This file contains the abstract class for factories.
'''
from abc import ABC, abstractmethod


class Factory(ABC):
    '''
        Abstract class for factories, 
        encapsulating objects that create instances of other other classes. 
    '''
    @abstractmethod
    def create():
        '''
            Abstract method for creating other classes.
        '''

    @abstractmethod
    def get():
        '''
            Abstract method for getting a stored instance.
        '''