'''
    This file contains the Logger class.
'''

from datetime import datetime

class Logger(object):
    '''
        A class for encapsulating the generation of logs.
    '''
    def __init__(self, log_file, auditor, encryption_service):
        self._log_file = log_file
        self._encryption_service = encryption_service
        self._auditor = auditor
    
    def log(self, loggable_information): # TODO: needs to assert shape of parameter
        '''
            A method for writing information about an action into a log file.

            loggable_information interface:
            {
                'user': user_name,
                'activity_type' : 'event' or 'action',
                'severity' : 'info' or 'warning' or 'danger',
                'action' : {
                    'type' : type,
                    'parameters' : action_parameters
                },
                'event' : {
                    'type' : type,
                    'parameters' : event_parameters
                }
            }
        '''
        with open(self._log_file, 'a') as file:
            # add timestamp
            timestamp = datetime.now().isoformat() # ISO 8601 format
            loggable_information['timestamp'] = timestamp
            # add severity
            if not loggable_information['severity']:
                loggable_information['severity'] = 'info'
            # encrypt sensitive data
            encrypted_information = self._encrypt(loggable_information)
            # store log
            file.write(f'{encrypted_information}\n') #JSON-lines format
        # audit logfile
        if additional_information := self._auditor.audit(self.log_file):
            #handle audit
            self.log(additional_information)

    def _encrypt(self, loggable_information):
        '''
            A method for encrypting sensitive data.
        '''
        activity_type = loggable_information['activity_type']
        # encrypt all parameters as might be sensitive 
        encrypted_parameters = {}
        for key, value in loggable_information[activity_type]['parameters']:
            encrypted_parameters[key] = self._encryption_service.encrypt(value)
        loggable_information[activity_type]['parameters'] = encrypted_parameters
        return encrypted_parameters
