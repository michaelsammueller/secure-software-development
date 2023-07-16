'''
    This file contains the Role class.
'''

import datetime
import time
import uuid


class Country:
    '''
        A parent class for the system countries.
    '''

    def get_country(self, id):
        if id:
            return self.__db_manager.do_select('SELECT * FROM countries WHERE id = ?', (id,))
        else:
            return False

    def get_country_id(self, name):
        result = self.__db_manager.do_select('SELECT id FROM roles WHERE name = ?', (name,))
        if len(result) >= 1:
            return result[0]['name']  # TODO
        else:
            return 0

    # Creates a record and returns the inserted id
    def add_country(self, code, name):
        if code and name:
            return self.__db_manager.do_insert(
                "INSERT INTO countries(uuid, code, name) VALUES (?, ?, ?) ",
                (str(uuid.uuid4()), code, name),  False)
        else:
            return False

    def update_country(self, id, name):
        # update the 'updated_at' attribute.
        self._updated_at = time.mktime(datetime.datetime.now().timetuple())
        # perform database query to update permission attributes.
        query = (
            "UPDATE countries SET name='" + name + "', "
            "updated_at= " + self._updated_at + " WHERE role_id=?")
        values = (id,)

        # call do_update method from DBmanager.
        self.__db_manager.do_update(query, values)

    def delete_country(self, id):
        # identify records to delete with id
        query = "DELETE FROM countries WHERE id = ?"
        where = (id,)
        # call do_delete method from DBManager
        return self.__db_manager.do_delete(query, where, False)

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.__db_manager = db_manager
