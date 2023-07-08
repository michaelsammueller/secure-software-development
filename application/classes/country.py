'''
    This file contains the Role class.
'''
import os
import sys

import datetime

# fpath = os.path.join(os.path.dirname(__file__).rstrip('classes'), 'data')
# #print(fpath)
# sys.path.append(fpath)

from dbmanager import DBManager
import uuid

class Country:
    '''
        A parent class for the system countries.
    '''

    def __init__(self, code = '', name = ''):
        # need id
        self._code = code  
        self._name = name       
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
        # initialise instance of DBManager
        self.db_manager = DBManager()

    def get_country(self, uuid):
        if uuid:
            return self.db_manager.do_select('SELECT * FROM countries WHERE uuid = ?', (uuid,) )
        else:
            return False
    
    # Creates a record and returns the inserted id
    def add_country(self, code, name):        
        if code and name:          
            return self.db_manager.do_insert("INSERT INTO countries(uuid, code, name) VALUES (?, ?, ?) ", (str(uuid.uuid4()), code, name),  False )  
        else:
            return False

    def update_country(self, uuid, name):
        # update the 'updated_at' attribute.
        self._updated_at = datetime.datetime.now()
        # perform database query to update permission attributes.
        query = "UPDATE countries SET name='" + name + "', updated_at= " + self._updated_at + " WHERE uuid=?"
        values = (uuid,)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_country(self, uuid):
        # identify records to delete with id
        query = "DELETE FROM countries WHERE uuid = ?"
        where = (uuid,)
        # call do_delete method from DBManager
        return self.db_manager.do_delete(query, where, False)      
  


# obj_country = Country()
# print( obj_country.add_country('US', 'USA') )
# rows = obj_country.get_country(1) 
# for row in rows:
#     print( dict(row) )