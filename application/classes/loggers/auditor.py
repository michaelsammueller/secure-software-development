'''
    This file contains the Auditor class.
'''


import json

class Auditor(object):
    '''
        A class for monitoring logs.
    '''
    def __init__(self, warning_file, danger_handler):
        self._warning_file = warning_file
        self._danger_handler = danger_handler
        self._severity_level = 'info' # alt states: 'warning', 'danger'
        self._new_log = {}
        self._num_lines_read = 0
        # severity parameters
        self._num_login_attempts = 0
        self._warning_login_attempts = 3
        self._danger_login_attempts = 6
    
    def audit(self, log_file, reset=False):
        '''
            A method for creating additional logs if needed.

            If a warning log is created, that will be stored in the warning file,
            with some decrypted information accessible to the moderator.

            If a danger log is created, that will be stored in the usual log file,
            containing encrypted sensitive information, accessible only to the superadmin.
        '''
        if reset:
            self._num_lines_read = 0
        with open(log_file, 'r') as file:
            for i, line in enumerate(file.readlines()):
                if i < self._num_lines_read:
                    continue
                else:
                    log = json.loads(line)
                    self._monitor_login_attempts(log)
                    if self._severity_level == 'warning':
                        self._warning_file.write(f'{self._new_log}\n')
                    if self._new_log:
                        new_log = self._new_log
                        self._severity_level = 'info' # reset
                        self._new_log = {} # reset
                        self._num_login_attempts = 0 # reset
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
            self._num_login_attempts += 1
            if self._num_login_attempts >= self._danger_login_attempts:
                self._severity_level = 'danger'
                self._new_log = {
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
                self._danger_handler.lockdown() # requires superadmin to unlock
            elif self._num_login_attempts >= self._warning_login_attempts:
                self._severity_level = 'warning' 
                self._new_log = {
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
            self._num_login_attempts = 0
