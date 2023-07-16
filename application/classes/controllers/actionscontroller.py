'''
    This file contains the ActionsController class.
'''


class ActionsController(object):
    '''
        A class for encapsulating a set of expected actions.
    '''
    def __init__(self):
        self.__ACTIONS = [
            'Add New User',
            'Delete User',
            'View All Users',
            'View User Details',
            'Update User Details',
            'Add Health Record',
            'Add Own Health Record',
            'View User Health Records',
            'View Own Health Records',
            'Delete User Health Records',
            'Edit Health Record',
            'View Temperature',
            'View Radiation Level',
            'Change Password',
            'Download Own Health Records'
        ]

        self.__ACTIONPARAMS = {
            'View Temperature': [('units', ['C', 'F', 'K'], 'ENUM')],
            'View Radiation Level': [('units', ['Rem', 'SV'], 'ENUM')],
            'Add New User': [('name', [], ''),
                             ('role', ['Astronaut', 'Moderator', 'Superadmin'], 'ROLE'),
                             ('date of birth', ['DD-MM-YYYY'], 'DATE'),
                             ('country of employment', [], 'COUNTRY'),
                             ('secret phrase', [], ''),
                             ('username', [], ''),
                             ('password', [], 'PASSWORD')],
            'Delete User': [('uuid', [], '')],
            'Add Own Health Record': [('complaints', [], ''),
                                      ('height', ['cm'], 'INT'),
                                      ('weight', ['kg'], 'INT'),
                                      ('blood_pressure', ['mmHg'], 'INT')],
            'Add Health Record': [('uuid', [], ''),
                                  ('complaints', [], ''),
                                  ('height', ['cm'], 'INT'),
                                  ('weight', ['kg'], 'INT'),
                                  ('blood_pressure', ['mmHg'], 'INT')],
            'View All Users': [],
            'View Own Health Records': [],
            'View User Details': [('uuid', [], '')],
            'View User Health Records': [('uuid', [], '')],
            'Delete User Health Records': [('uuid', [], '')],
            'Update User Details': [('uuid', [], ''),
                                    ('field', ['name', 'role',
                                               'date of birth', 'country of employment'],
                                     'ENUM'),
                                    ('new value', [], '')],  # VULNERABILITY (bypasses sanitisation)
            'Edit Health Record': [('record id', [], ''),
                                   ('field', ['complaints', 'weight',
                                              'height', 'blood pressure'],
                                    'ENUM'),
                                   ('new value', [], '')],  # VULNERABILITY (bypasses sanitisation)
            'Change Password': [],
            'Download Own Health Records': [],
        }

    def get_actions(self):
        '''
            This returns a list of actions filtered by the role of the user.
        '''
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        key = lambda action: self.__authorisation_service.check_permission(action, user_role)
        filtered_actions = filter(key, self.__ACTIONS)
        return list(filtered_actions)

    def get_action_params(self, action):
        '''
            The return value consists of a list of fields.
            Each field is a tuple of the form (field_name, field_options).
            if field_options is empty, then no options are provided.
        '''
        return self.__ACTIONPARAMS[action]

    def __call__(self, action, parameters):
        '''
            A method for calling an action.
        '''
        if action not in self.__ACTIONS:
            return False
        func_map = {
            'Add New User': self.add_new_user,
            'Delete User': self.delete_user,
            'Add Health Record': self.add_health_record,
            'Add Own Health Record': self.add_own_health_record,
            'View Temperature': self.view_temperature,
            'View Radiation Level': self.view_radiation_level,
            'View All Users': self.view_all_users,
            'View User Details': self.view_user,
            'View Own Health Records': self.view_own_health_records,
            'View User Health Records': self.view_users_health_records,
            'Delete User Health Records': self.delete_user_health_records,
            'Update User Details': self.update_user_information,
            'Edit Health Record': self.update_health_record,
            'Change Password': self.change_password,
            'Download Own Health Records': self.download_health_records,
        }
        return func_map[action](parameters)

    def add_new_user(self, new_user_details):
        '''
            A method for adding a user to the system.

            new_user_details interface:
            {
                'name': name,
                'role': 'astronaut' or 'moderator' or 'superadmin',
                'date of birth': 'DD-MM-YYYY',
                'country of employment': country,
                'secret phrase' : phrase
                'username': username,
                'password': password
            }
        '''
        action = 'Add New User'
        # assert shape of parameter
        if not self.assert_params_shape(new_user_details, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        if self.__user_service.add_user(new_user_details):
            results = {'Confirmation': 'User Added'}
        else:
            results = {'Error': 'User Not Added'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': {
                    key: value for key, value in new_user_details.items()
                },
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def view_all_users(self, *args, **kwargs):
        '''
            A method for viewing all users of the system.
        '''
        action = 'View All Users'
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        results = self.__user_service.view_all_users()
        if not results:
            results = {'Error': 'No Users Found'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': {},
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def view_user(self, user_identifiers):
        '''
            A method for viewing a user of the system.

            user_identifiers interface:
            {
                'uuid': uuid,
            }
        '''
        action = 'View User Details'
        # assert shape of parameter
        if not self.assert_params_shape(user_identifiers, action):
            return {'Error': 'Invalid parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        results = self.__user_service.view_user(user_identifiers)
        if not results:
            results = {'Error': 'No Users Found'}
        else:
            results = {key: str(value) for key, value in results.items()}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': user_identifiers,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def delete_user(self, old_user_identifiers):
        '''
            A method for deleting a user from the system.

            old_user_details interface:
            {
                'uuid': uuid,
            }
        '''
        action = "Delete User"
        # assert shape of parameter
        if not self.assert_params_shape(old_user_identifiers, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        # TODO clarify whether user was deleted or not
        if self.__user_service.delete_user(old_user_identifiers):
            results = {'Confirmation': 'User Deleted'}
        else:
            results = {'Error': 'User Not Deleted'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': old_user_identifiers,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def update_user_information(self, new_information):
        '''
            A method for deleting a user from the system.

            old_user_details interface:
            {
                'uuid': uuid,
                'field': ['name', 'role', 'date of birth', 'country of employment'],
                'new value': 'new value'
            }
        '''
        action = "Update User Details"
        # assert shape of parameter
        if not self.assert_params_shape(new_information, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        if self.__user_service.update_user(new_information):
            results = {'Confirmation': 'User Details Updated'}
        else:
            results = {'Error': 'User Details Not Updated'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': new_information,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def add_health_record(self, new_health_record_details):
        '''
            A method for adding health record details to the system about a user.

            new_user_details interface:
            {
                'uuid': uuid,
                'complaints' : complaints
                'height': height,
                'weight': weight,
                'blood_pressure': blood_pressure,
            }
        '''
        action = 'Add Health Record'
        if not self.assert_params_shape(new_health_record_details, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        if self.__health_record_service.add_record(new_health_record_details):
            results = {'Confirmation': 'Health Record Added'}
        else:
            results = {'Error': 'Health Record Not Added'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': new_health_record_details,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def add_own_health_record(self, new_health_record_details):
        '''
            A method for adding own health record details to the system about a user.

            new_user_details interface:
            {
                'complaints' : complaints
                'height': height,
                'weight': weight,
                'blood_pressure': blood_pressure,
            }
        '''
        action = 'Add Own Health Record'
        if not self.assert_params_shape(new_health_record_details, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        new_health_record_details['uuid'] = self.__user_service.get_user_uuid(
            self.__login_service.get_loggedin_username())
        if self.__health_record_service.add_record(new_health_record_details):
            results = {'Confirmation': 'Health Record Added'}
        else:
            results = {'Error': 'Health Record Not Added'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': new_health_record_details,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def view_users_health_records(self, user_identifiers):
        '''
            A method for viewing the health records about a user.

            user_identifiers interface:
            {
                'uuid': uuid,
            }
        '''
        action = 'View User Health Records'
        # assert shape of parameter
        if not self.assert_params_shape(user_identifiers, action):
            return {'Error': 'Invalid parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        results = self.__health_record_service.view_user_health_records(user_identifiers)
        if not results:
            log_results = {'Error': 'No Health Records Found'}
            display_results = log_results
        else:
            log_results = {'Confirmation': 'Health Records Viewed'}
            display_results = [
                {key: str(value) for key, value in result.items()} for result in results]
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': user_identifiers,
                'results': log_results
            }
        }
        self.__logger.log(json)
        # return results
        return display_results

    def view_own_health_records(self, *args, **kwargs):
        '''
            A method for viewing the health records about a user.
        '''
        action = 'View Own Health Records'
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        user_identifiers = {'uuid': self.__user_service.get_user_uuid(
            self.__login_service.get_loggedin_username())}
        results = self.__health_record_service.view_user_health_records(user_identifiers)
        if not results:
            log_results = {'Error': 'No Health Records Found'}
            display_results = log_results
        else:
            log_results = {'Confirmation': 'Health Records Viewed'}
            display_results = [
                {key: str(value) for key, value in result.items()} for result in results]
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': user_identifiers,
                'results': log_results
            }
        }
        self.__logger.log(json)
        # return results
        return display_results

    def delete_user_health_records(self, user_identifiers):
        '''
            A method for deleting the health records about a user.

            user_identifiers interface:
            {
                'uuid': uuid,
            }
        '''
        action = 'Delete User Health Records'
        # assert shape of parameter
        if not self.assert_params_shape(user_identifiers, action):
            return {'Error': 'Invalid parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        if self.__health_record_service.delete_user_health_records(user_identifiers):
            results = {'Confirmation': 'Health Records Deleted'}
        else:
            results = {'Error': 'Health Records Not Deleted'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': user_identifiers,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

    def update_health_record(self, new_information):
        '''
            A method for deleting a user from the system.

            old_user_details interface:
            {
                'record id': id,
                'field': ['complaints', 'height', 'weight', 'blood_pressure],
                'new value': 'new value'
            }
        '''
        action = "Edit Health Record"
        # assert shape of parameter
        if not self.assert_params_shape(new_information, action):
            return {'Error': 'Missing parameters'}
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        if self.__health_record_service.update_health_record(new_information):
            results = {'Confirmation': 'Health Record Updated'}
        else:
            results = {'Error': 'Health Record Not Updated'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': new_information,
                'results': results
            }
        }
        self.__logger.log(json)
        # return results
        return results

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
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        temperature = self.__thermometer.read_data(measurement_details['units'])
        units = self.__thermometer.get_units()
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': measurement_details,
                'results': {
                    'temperature': temperature,
                    'units': units
                }
            }
        }
        self.__logger.log(json)
        # return results
        return {"temperature": temperature, "units": units}

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
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # perform action
        radiation = self.__geiger_counter.read_data(measurement_details['units'])
        units = self.__geiger_counter.get_units()
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': measurement_details,
                'results': {
                    'radiation': radiation,
                    'units': units
                }
            }
        }
        self.__logger.log(json)
        # return results
        return {"radiation": radiation, "units": units}

    def change_password(self, *args, **kwargs):
        '''
            A method for changing passwords.
        '''
        action = 'Change Password'
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(
            self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # log action
        json = {
            'user': self.__login_service.get_loggedin_username(),
            'activity_type': 'action',
            'action': {
                'type': action,
                'parameters': {},
                'results': {}
            }
        }
        self.__logger.log(json)
        # perform action
        self.__cli.change_password()
        # return results
        return {}
    
    def download_health_records(self, *args, **kwargs):
        '''
            A method for changing passwords.
        '''
        action = 'Download Own Health Records'
        # assert permission for action
        user_role = self.__authorisation_service.get_user_role(self.__login_service.get_loggedin_username())
        if not self.__authorisation_service.check_permission(action, user_role):
            return {'Error': 'Unauthorised action'}
        # log action
        json = {
            'user' : self.__login_service.get_loggedin_username(),
            'activity_type' : 'action',
            'action' : {
                'type' : action,
                'parameters' : {},
                'results' : {}
            }
        }
        self.__logger.log(json)
        # perform action
        self.__download_service.download()
        # return results
        return {}

    def assert_params_shape(self, parameters, action):
        '''
            A method for checking all details were provided for action.
        '''
        try:
            fields = self.__ACTIONPARAMS[action]
            all(parameters[field[0]] for field in fields)
            return True
        except KeyError:
            json = {
                'user': self.__login_service.get_loggedin_username(),
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'Missing Parameters',
                    'details': {
                        'action': action,
                        'provided_parameters': {key: value for key, value in parameters.items()},
                        'required_parameters': [field[0] for field in fields]
                    }
                }
            }
            self._logger.log(json)
            return False

    def connect_logger(self, logger):
        """Connects the logger"""
        self.__logger = logger

    def connect_authorisation_service(self, authorisation_service):
        """Connects the authorisation service"""
        self.__authorisation_service = authorisation_service

    def connect_user_service(self, user_service):
        """Connects the loggined in user"""
        self.__user_service = user_service

    def connect_thermometer(self, thermometer):
        """Connects the thermometer"""
        self.__thermometer = thermometer

    def connect_geiger_counter(self, geiger_counter):
        """Connects the geiger counter"""
        self.__geiger_counter = geiger_counter

    def connect_health_record_service(self, health_record_service):
        """Connects the record service"""
        self.__health_record_service = health_record_service

    def connect_login_service(self, login_service):
        """Connects the record service"""
        self.__login_service = login_service

    def connect_download_service(self, download_service):
        """Connects the download service"""
        self.__download_service = download_service

    def connect_cli(self, cli):
        """Connects the cli"""
        self.__cli = cli
