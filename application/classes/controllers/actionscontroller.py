'''
    This file contains the ActionsController class.
'''

class ActionsController(object):
    '''
        A class for encapsulating a set of expected actions.
    '''
    def __init__(self):
        self._ACTIONS = [
            'Add New User', # TODO
            'Delete User', # TODO
            'Add Health Record', # TODO
            'View Health Record', # TODO
            'Execute SQL Query', # TODO
            'View Warning Logs', # TODO
            'View All Logs', # TODO
            'View Temperature',
            'View Radiation Level',
            'Update Health Record', # TODO
            'Delete Health Record', # TODO
        ]
        self._ACTIONPARAMS = {
            'View Temperature': [('units', ['C', 'F', 'K'])],
            'View Radiation Level': [('units', ['Rem', 'SV'])],
            'Add New User': [('user_name', []), 
                             ('user_role', ['astronaut', 'moderator', 'superadmin'])],
        }


    def get_actions(self):
        user_role = self.user.get_role()
        key = lambda action: self.authorisation_service.check_permission(action, user_role)
        filtered_actions = filter(key, self._ACTIONS)
        return list(filtered_actions)
    
    def get_action_params(self, action):
        '''
            The return value consists of a list of fields. 
            Each field is a tuple of the form (field_name, field_options).
            if field_options is empty, then no options are provided.'''
        return self._ACTIONPARAMS[action]
    
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
            'View Health Record': self.view_health_record,
            'Execute SQL Query': self.input_raw_sql,
            'View Temperature': self.view_temperature,
            'View Radiation Level': self.view_radiation_level
        }
        return func_map[action](parameters)

    def add_new_user(self, new_user_details): #TODO
        '''
            A method for adding a user to the system.

            new_user_details interface:
            {
                'user_name': user_name,
                'user_role': 'astronaut' or 'moderator' or 'superadmin',
            }
        '''
        action = 'Add New User'
        if not self.assert_params_shape(new_user_details, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        if not self.authorisation_service.check_permission(action, self.user.get_role()):
            return {'Error': 'Unauthorised action'}
        # perform action
        # results = self.db.do_insert('users', new_user_details) TODO: pass details to database
        # log action
        json = {
            'user' : self.user.get_name(),
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'parameters' : {
                    key : value for key, value in new_user_details.items()
                },
                'results' : results
            }
        }
        self._logger.log(json)
        # return results
        return results

    def delete_user(self, old_user_details): #TODO
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

    def add_health_record(self, new_health_record_details): #TODO
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

    def view_health_record(self, request_details): #TODO
        '''
            A method for viewing the health records about a user.
        '''
        pass

    def input_raw_sql(self, sql_query): #TODO
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

    def view_temperature(self, measurement_details):
        '''
            A method for viewing the readings of a thermometer.

            measurement_details interface:
            {
                'units': 'C' or 'F or 'K
            }
        '''
        action = 'View Temperature'
        # assert shape of parameter
        if not self.assert_params_shape(measurement_details, action):
            return {'Error': 'Invalid parameters'}
        # assert permission for action
        if not self.authorisation_service.check_permission(action, self.user.get_role()):
            return {'Error': 'Unauthorised action'}
        # perform action
        temperature = self.thermometer.read_data(measurement_details['units'])
        units = self.thermometer.get_units()
        # log action
        json = {
            'user' : self.user.get_name(),
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'results' : {
                    'temperature' : temperature,
                    'units' : units
                }
            }
        }
        self.logger.log(json)
        # return results
        return json['action']['results']
    
    def view_radiation_level(self, measurement_details):
        '''
            A method for viewing the readings of a gieger counter.

            measurement_details interface:
            {
                'units': 'Rem' or 'SV'
            }
        '''
        action = 'View Radiation Level'
        # assert shape of parameter
        if not self.assert_params_shape(measurement_details, action):
            return {'Error': 'Invalid parameters'}
        # assert permission for action
        if not self.authorisation_service.check_permission(action, self.user.get_role()):
            return {'Error': 'Unauthorised action'}
        # perform action
        radiation = self.geiger_counter.read_data(measurement_details['units'])
        units = self.geiger_counter.get_units()
        # log action
        json = {
            'user' : self.user.get_name(),
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'results' : {
                    'radiation' : radiation,
                    'units' : units
                }
            }
        }
        self.logger.log(json)
        # return results
        return json['action']['results']

    def assert_params_shape(self, parameters, action):
        '''
            A method for checking all details were provided for action.
        '''
        try:
            fields = self._ACTIONPARAMS[action]
            all(parameters[field[0]] for field in fields)
            return True
        except KeyError:
            json = {
                'user' : self.user.get_name(),
                'activity_type' : 'event',
                'severity' : 'warning',
                'event' : {
                    'type' : 'Missing Parameters',
                    'details' : {
                        'action' : action,
                        'parameters' : {key : value for key, value in parameters.items()},
                        'required' : [field[0] for field in fields]
                    }
                }
            }
            self._logger.log(json)
            return False

    def connect_logger(self, logger):
        """Connects the logger"""
        self.logger = logger

    def connect_dbms(self, dbms):
        """Connects the database management service"""
        self.dbms = dbms

    def connect_authorisation_service(self, authorisation_service):
        """Connects the authorisation service"""
        self.authorisation_service = authorisation_service

    def connect_user(self, user):
        """Connects the action controller"""
        self.user = user

    def connect_thermometer(self, thermometer):
        """Connects the action controller"""
        self.thermometer = thermometer
    
    def connect_geiger_counter(self, geiger_counter):
        """Connects the action controller"""
        self.geiger_counter = geiger_counter