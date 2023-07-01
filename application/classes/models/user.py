'''
    This file contains the User class.
'''
import datetime
import time
import uuid

class User:
    '''
        A class to create user objects.
    '''
    def __init__(self, details):
        self.__name = details['name']
        self.__code = details['code'] # CLARIFY
        self.__dob = details['date of birth'] # CLARIFY
        self.__role_id = details['role']
        self.__country_id = details['country of employment']
        self.__username = details['username']
        self.__password = details['password']
        self.__uuid = uuid.uuid4()
        self.__created_at = None
        self.__updated_at = None
        self.__last_login_at = None

    def add_user(self):
        # update created_at and updated_at attributes
        if self.__created_at is None:
            self.__created_at = time.mktime(datetime.datetime.now().timetuple())
        self.__updated_at = time.mktime(datetime.datetime.now().timetuple())

        # perform database query to save user attributes.
        query = "INSERT INTO users (uuid, name, code, dob, role_id, \
            country_id, username, password) VALUES ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (str(self.__uuid), self.__name, self.__code, self.__dob, self.__role_id,
                  self.__country_id, self.__username, self.__password, self.__created_at)

        # call do_insert method from DBmanager.
        self.db_manager.do_insert(query, [values], dry=False)

    def update_user(self):
        # update the 'updated_at' attribute.
        self._updated_at = time.mktime(datetime.datetime.now().timetuple())

        # perform database query to update user attributes.
        query = "UPDATE users SET name=?, code=?, dob=?, role_id=?, \
            country_id=?, username=?, password=?, updated_at=? WHERE uuid=?"
        values = (self.__name, self.__code, self.__dob, self.__role_id, self.__country_id,
                  self.__username, self.__password, self.__updated_at, str(self.__uuid))

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_user(self):
        pass

    def login_user(self):
        self.__last_login_at = time.mktime(datetime.datetime.now().timetuple())
                # perform database query to save user attributes.
        query = "INSERT INTO users (uuid, name, code, dob, role_id, \
            country_id, username, password) VALUES ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (str(self.__uuid), self.__name, self.__code, self.__dob, self.__role_id,
                  self.__country_id, self.__username, self.__password, self.__created_at)

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.db_manager = db_manager

    def connect_role_service(self, role_service):
        '''
            A method for connecting the role.
        '''
        self.role_service = role_service
        if type(self.__role_id) is str:
            self.__role_id = self.role_service.get_role_id(self.__role_id)
    
    def connect_country_service(self, country_service):
        '''
            A method for connecting the country.
        '''
        self.country_service = country_service
        if type(self.__country_id) is str:
            self.__country_id = self.country_service.get_country_id(self.__country_id)
