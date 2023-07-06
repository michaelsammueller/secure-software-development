'''
    This file contains the Auditor class.
'''

import json

class Auditor(object):
    '''
        A class for monitoring logs.
    '''
    def __init__(self, warning_file):
        self.__warning_file = warning_file
        self.__severity_level = 'info' # alt states: 'warning', 'danger'
        self.__new_log = {}
        self.__num_lines_read = 0
        # severity parameters
        self.__num_login_attempts = 0
        self.__warning_login_attempts = 3
        self.__danger_login_attempts = 6
    
    def audit(self, log_file, reset=False):
        '''
            A method for creating additional logs if needed.

            If a warning log is created, that will be stored in the warning file,
            with some decrypted information accessible to the moderator.

            If a danger log is created, that will be stored in the usual log file,
            containing encrypted sensitive information, accessible only to the superadmin.
        '''
        if reset:
            self.__num_lines_read = 0
        with open(log_file, 'r') as file:
            for i, line in enumerate(file.readlines()):
                if i < self.__num_lines_read:
                    continue
                else:
                    log = json.loads(line)
                    self._monitor_login_attempts(log)
                    if self.__severity_level == 'warning':
                        self.__warning_file.write(f'{self.__new_log}\n')
                    if self.__new_log:
                        new_log = self.__new_log
                        self.__severity_level = 'info' # reset
                        self.__new_log = {} # reset
                        self.__num_login_attempts = 0 # reset
                        return new_log
    
    def _monitor_login_attempts(self, log):
        '''
            A method for monitoring login attempts.

            If warning level is reached, a warning log is created
            containing the inputted username readable
            by moderator. 
            
            If danger level is reached, an encyrpted danger 
            log is created containing inputted username and password.
            All future logins will be blocked until superadmin has logged in
            and reset danger level. 
        '''
        if log['activity_type'] == 'action' and log['action']['type'] == 'login':
            self.__num_login_attempts += 1
            if self.__num_login_attempts >= self.__danger_login_attempts:
                self.__severity_level = 'danger'
                self.__new_log = {
                    'user' : log['user'],
                    'activity_type' : 'event',
                    'severity' : 'danger',
                    'event' : {
                        'type' : 'login_attempts_danger',
                        'parameters' : {
                            'username' : log['action']['parameters']['username'],
                            'password' : log['action']['parameters']['password']
                        }
                    }
                }
                self.__danger_handler.lockdown() # requires superadmin to unlock
            elif self.__num_login_attempts >= self.__warning_login_attempts:
                self.__severity_level = 'warning' 
                self.__new_log = {
                    'user' : log['user'],
                    'activity_type' : 'event',
                    'severity' : 'warning',
                    'event' : {
                        'type' : 'login_attempts_warning',
                        'parameters' : {
                            'username' : log['action']['parameters']['username'],
                        }
                    }
                }
        elif log['activity_type'] == 'event':
            pass
        else:
            self.__num_login_attempts = 0

    def connect_danger_handler(self, danger_handler):
        '''
            A method for connecting the auditor to the danger handler.
        '''
        self.__danger_handler = danger_handler
