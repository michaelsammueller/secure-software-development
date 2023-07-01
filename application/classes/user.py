'''
    This file contains the User class.
'''
import uuid
import os
import sys
import datetime
fpath = os.path.join(os.path.dirname(__file__).rstrip('classes'), 'data')
sys.path.append(fpath)
from dbmanager import DBManager

class User:
    '''
        A class to create user objects.
    '''
    def __init__(self, name, code, dob, role_id, country_id, username, password):
        self.__name = name
        self.__code = code
        self.__dob = dob
        self.__role_id = role_id
        self.__country_id = country_id
        self.__username = username
        self.__password = password
        self.__uuid = uuid.uuid4()
        self.__created_at = None
        self.__updated_at = None
        self.__last_login_at = None

        # initialise instance of DBManager
        self.db_manager = DBManager()

        # set current_time to now
        self.current_time = datetime.datetime.now()

    def add_user(self):
        # update created_at and updated_at attributes
        if self._created_at is None:
            self._created_at = self.current_time
        self._updated_at = self.current_time

        # perform database query to save user attributes.
        query = "INSERT INTO users (uuid, name, code, dob, role_id, \
            country_id, username, password) VALUES ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (str(self._uuid), self._name, self._code, self._dob, self._role_id,
                  self._country_id, self._username, self._password, self._created_at)

        # call do_insert method from DBmanager.
        self.db_manager.do_insert(query, [values], dry=False)

    def update_user(self):
        # update the 'updated_at' attribute.
        self._updated_at = self.current_time

        # perform database query to update user attributes.
        query = "UPDATE users SET name=?, code=?, dob=?, role_id=?, \
            country_id=?, username=?, password=?, updated_at=? WHERE uuid=?"
        values = (self._name, self._code, self._dob, self._role_id, self._country_id,
                  self._username, self._password, self._updated_at, str(self._uuid))

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_user(self):
        pass
