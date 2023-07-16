'''
    This file contains the Logger class.
'''

from datetime import datetime
import json

class Logger(object):
    '''
        A class for encapsulating the generation of logs.
    '''
    def __init__(self, log_file):
        self.__log_file = log_file
    
    def log(self, loggable_information):
        '''
            A method for writing information about an action into a log file.

            loggable_information interfaces:
            {
                'user': user_name,
                'activity_type' : 'action',
                'severity' : 'info' or 'warning' or 'danger',
                'action' : {
                    'type' : type,
                    'parameters' : action_parameters
                    'results' : action_results
                }
            }
            or
            {
                'user': user_name,
                'activity_type' : 'event',
                'severity' : 'info' or 'warning' or 'danger',
                'event' : {
                    'type' : type,
                    'details' : {}
                }
            }
        '''
        with open(self.__log_file, 'a') as file:
            # add timestamp
            timestamp = datetime.now().isoformat() # ISO 8601 format
            loggable_information['timestamp'] = timestamp
            # add severity
            if not 'severity' in loggable_information.keys():
                loggable_information['severity'] = 'info'
            # encrypt sensitive data
            encrypted_information = self.encrypt(loggable_information)
            # store log
            json_line = json.dumps(encrypted_information)
            file.write(f'{json_line}\n') #JSON-lines format
        # audit logfile
        if additional_information := self.__auditor.audit(self.__log_file):
            #handle audit
            self.log(additional_information)

    def encrypt(self, loggable_information):
        '''
            A method for encrypting sensitive data.
        '''
        activity_type = loggable_information['activity_type']
        # encrypt all parameters as might be sensitive 
        if activity_type == 'action':
            encrypted_information = {'parameters': {}, 'results': {}}
            for key, value in loggable_information['action']['parameters'].items():
                encrypted_information['parameters'][key] = self.__encryption_service.encrypt(value)
            loggable_information[activity_type]['parameters'] = encrypted_information['parameters']
            try:
                for key, value in loggable_information['action']['results'].items():
                    encrypted_information['results'][key] = self.__encryption_service.encrypt(value)
            except:
                encrypted_information['results'] = []
                for result in loggable_information['action']['results']:
                    encrypted_entry = {}
                    for key, value in result.items():
                        encrypted_entry[key] = self.__encryption_service.encrypt(value)
                    encrypted_information['results'].append(encrypted_entry)
            finally:
                loggable_information['action']['results'] = encrypted_information['results']
        elif activity_type == 'event':
            encrypted_information = {'details': {}}
            for key, value in loggable_information['event']['details'].items():
                encrypted_information['details'][key] = self.__encryption_service.encrypt(value)
            loggable_information[activity_type]['details'] = encrypted_information['details']
        return loggable_information
    
    def connect_encryption_service(self, encryption_service):
        '''
            A method for connecting the encryption service.
        '''
        self.__encryption_service = encryption_service

    def connect_auditor(self, auditor):
        '''
            A method for connecting the auditor.
        '''
        self.__auditor = auditor
