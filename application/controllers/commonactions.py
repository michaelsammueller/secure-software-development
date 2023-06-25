'''
    This file contains the CommonActions class.
'''

class CommonActions(object):
    '''
        A class for encapsulating a set of expected actions.
    '''
    def __init__(self, logger, db, login_service, authorisation_service):
        self._logger = logger
        self._login_service = login_service
        self._authorisation_service = authorisation_service
        self._db = db

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
        user = self._login_service.get_logged_in_user()
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
        return self._db.insert('users', new_user_details)

    def delete_user(self, old_user_details):
        '''
            A method for deleting a user from the system.
        '''
        action = 'delete_user'
        user = self._login_service.get_logged_in_user()
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
        return self._db.delete('users', old_user_details)

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
        user = self._login_service.get_logged_in_user()
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
        return self._db.insert('users', new_health_record_details)

    def view_health_records(self, request_details):
        '''
            A method for viewing the health records about a user.
        '''
        pass

    def input_raw_sql(self, sql_query):
        '''
            A method for querying the system using raw sql.
        '''
        action = 'input_raw_sql'
        user = self._login_service.get_logged_in_user()
        # assert permission for action
        if not self._authorisation_service.check_permission(action, user):
            return False
        # log action
        self._logger.log({
            'user' : self._login_service.get_logged_in_user(),
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