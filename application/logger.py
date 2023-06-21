'''
    This file contains the Logger class.
'''


class Logger(object):
    '''
        A class for encapsulating the generation of logs.
    '''
    def __init__(self, log_file):
        self._log_file = log_file
    
    def log(self, loggable_information):
        '''
            A method for writing information about an action into a log file.
        '''
        pass
