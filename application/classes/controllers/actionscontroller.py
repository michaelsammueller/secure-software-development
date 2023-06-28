'''
    This file contains the ActionsController class.
'''

class ActionsController(object):
    '''
        A class for encapsulating a set of expected actions.
    '''
    def __init__(self, logger, db, user, authorisation_service):
        self._logger = logger
        self._user = user
        self._authorisation_service = authorisation_service
        self._db = db
        self._ACTIONS = [
            'Add New User',
            'Delete User',
            'Add Health Record',
            'View Health Record',
            'Execute SQL Query',
            'View Warning Logs', # TODO
            'View All Logs', # TODO
            'View Temperature', # TODO
            'View Radiation Levels', # TODO
            'Update Health Record', # TODO
            'Delete Health Record', # TODO
            ''
        ]

    def get_actions(self):
        return self._ACTIONS
    
    def __call__(self, action, parameters):
        '''
            A method for calling an action.
        '''
        if action not in self._ACTIONS:
            return False
        func_map  = {
            'Add New User': self.add_new_user,
            'Delete User': self.delete_user,
            'Add Health Record': self.add_health_record,
            'View Health Record': self.view_health_records,
            'Execute SQL Query': self.input_raw_sql,
            'View Temperature': self.view_temperature,
        }
        return func_map[action](parameters)

    def add_new_user(self, new_user_details):
        '''
            A method for adding a user to the system.

            new_user_details interface:
            {
                'user_name': user_name,
                'user_role': 'astronaut' or 'moderator' or 'superadmin',
            }
        '''
        action = 'add_new_user'
        user = self._user.get_name()
        # assert shape of parameter
        try:
            all(new_user_details['user_name'], 
                new_user_details['user_role'])
        except KeyError:
            self._logger.log({
                'user' : user,
                'activity_type' : 'event',
                'severity' : 'warning',
                'event' : {
                    'type' : 'add_new_user_key_error',
                    'parameters' : {
                        key : value for key, value in new_user_details.items()
                    }
                }
            })
            return False
        # assert permission for action
        if not self._authorisation_service.check_permission(action, user):
            return False
        # log action
        self._logger.log({
            'user' : user,
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'parameters' : {
                    key : value for key, value in new_user_details.items()
                }
            }
        })
        # add user to database
        return self._db.do_insert('users', new_user_details)

    def delete_user(self, old_user_details):
        '''
            A method for deleting a user from the system.
        '''
        action = 'delete_user'
        user = self._user.get_name()
        # assert permission for action
        if not self._authorisation_service.check_permission(action, user):
            return False
        # log action
        self._logger.log({
            'user' : user,
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'parameters' : {
                    key : value for key, value in old_user_details.items()
                }
            }
        })
        # delete user from database
        return self._db.do_delete('users', old_user_details)

    def add_health_record(self, new_health_record_details):
        '''
            A method for adding health record details to the system about a user.

            new_user_details interface:
            {
                'user_name': user_name,
                'height'?: height,
                'weight'?: weight,
                'blood_type'?: blood_type,
                'blood_pressure'?: blood_pressure,
                'heart_rate'?: heart_rate,
                'body_temperature'?: body_temperature,
                'diary_entry'?: diary_entry
            }
        '''
        action = 'add_new_health_record'
        user = self._user.get_name()
        # assert shape of parameter
        try:
            all(new_health_record_details['user_name'])
        except KeyError:
            self._logger.log({
                'user' : user,
                'activity_type' : 'event',
                'severity' : 'warning',
                'event' : {
                    'type' : 'add_new_health_record_key_error',
                    'parameters' : {
                        key : value for key, value in new_health_record_details.items()
                    }
                }
            })
            return False
        # assert permission for action
        if not self._authorisation_service.check_permission(action, user):
            return False
        # log action
        self._logger.log({
            'user' : user,
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'parameters' : {
                    key : value for key, value in new_health_record_details.items()
                }
            }
        })
        # add user to database
        return self._db.do_insert('users', new_health_record_details)

    def view_health_record(self, request_details):
        '''
            A method for viewing the health records about a user.
        '''
        pass

    def input_raw_sql(self, sql_query):
        '''
            A method for querying the system using raw sql.
        '''
        action = 'input_raw_sql'
        user = self._user.get_name()
        # assert permission for action
        if not self._authorisation_service.check_permission(action, user):
            return False
        # log action
        self._logger.log({
            'user' : self._user.get_name(),
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'parameters' : {
                    'sql_query' : sql_query
                }
            }
        })
        # execute sql
        return self._db.execute(sql_query)

    def view_temperature(self):
        '''
            A method for viewing the readings of a thermometer.
        '''
        pass