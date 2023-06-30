'''
    This file contains the User class.
'''
import uuid
import dbmanager
import datetime


class User:
    '''
        A class to create user objects.
    '''
    def __init__(self, name, code, dob, role_id, country_id, username, password):
        self._name = name
        self._code = code
        self._dob = dob
        self._role_id = role_id
        self._country_id = country_id
        self._username = username
        self._password = password
        self._uuid = uuid.uuid4()
        self._created_at = None
        self._updated_at = None
        self._last_login_at = None

        # initialise instance of DBManager
        self.db_manager = dbmanager.DBManager()

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
