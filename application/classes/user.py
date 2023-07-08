'''
    This file contains the User class.
'''
# leave imports in for now
import uuid
import os
import sys
fpath = os.path.join(os.path.dirname(__file__).rstrip('classes'), 'data')
sys.path.append(fpath)
from dbmanager import DBManager

class User:
    '''
        A class to create user objects.
    '''

    def add_user(self, name, code, dob, role_id, country_id, username, password):
        # perform database query to save user attributes.
        query = "INSERT INTO users (uuid, name, code, dob, role_id, \
            country_id, username, password, updated_at) \
                VALUES ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (str(uuid.uuid4()), name, code, dob, role_id,
                  country_id, username, password)

        # call do_insert method from DBmanager.
        self.__db_manager.do_insert(query, [values], dry=False)

    def update_user(self):
        # update the 'updated_at' attribute.
        self.__updated_at = self.__current_time

        # perform database query to update user attributes.
        query = "UPDATE users SET name=?, code=?, dob=?, role_id=?, \
            country_id=?, username=?, password=?, updated_at=? WHERE uuid=?"
        values = (self.__name, self.__code, self.__dob, self.__role_id, self.__country_id,
                  self.__username, self.__password, self.__updated_at, str(self.__uuid))

        # call do_update method from DBmanager.
        self.__db_manager.do_update(query, values)

    def delete_user(self, uuid):
        # perform database query to identify row to delete
        query = "DELETE FROM users WHERE uuid=?"
        values = uuid
        
        # call do_delete method from DBmanager
        self.__db_manager.do_delete(query, values)
