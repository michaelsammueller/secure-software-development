'''
    This file contains the User class.
'''
import uuid

class User:
    '''
        A class to create user objects.
    '''

    def add_user(self, user_details):
        # perform database query to save user attributes.
        query = "INSERT INTO users (uuid, name, code, dob, role_id, \
            country_id, username, password) VALUES ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (str(uuid.uuid4()), user_details['name'], user_details['code'], user_details['date of birth'], user_details['role'],
                  user_details['country of employment'], user_details['username'], user_details['password'])

        # call do_insert method from DBmanager.
        self.db_manager.do_insert(query, [values], dry=False)


    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.db_manager = db_manager

    def connect_role_service(self, role_service):
        '''
            A method for connecting the role service.
        '''
        self.role_service = role_service
    
    def connect_country_service(self, country_service):
        '''
            A method for connecting the country service.
        '''
        self.country_service = country_service

