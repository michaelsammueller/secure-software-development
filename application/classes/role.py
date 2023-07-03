'''
    This file contains the Role class.
'''
import os
import sys
import datetime
fpath = os.path.join(os.path.dirname(__file__).rstrip('classes'), 'data')
#print(fpath)
sys.path.append(fpath)
from dbmanager import DBManager
import uuid

class Role:
    '''
        A parent class for the system roles.
    '''

    def __init__(self, name = ''):
        # need id
        self._name = name       
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
        # initialise instance of DBManager
        self.db_manager = DBManager()

    def get_role(self, uuid):
      
        if uuid:
            return self.db_manager.do_select('SELECT * FROM roles WHERE uuid = ?', (uuid,) )
        else:
            return False
    
    # Creates a record and returns the inserted id
    def add_role(self, name):        
        if name:          
            return self.db_manager.do_insert("INSERT INTO roles(uuid, name) VALUES (?, ?) ", (str(uuid.uuid4()), name),  False )  
        else:
            return False

    def update_role(self, uuid, name):
        # update the 'updated_at' attribute.
        self._updated_at = datetime.datetime.now()
        # perform database query to update permission attributes.
        query = "UPDATE roles SET name='" + name + "', updated_at= " + self._updated_at + " WHERE uuid=?"
        values = (uuid,)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_role(self, uuid):
        # identify records to delete with uuid
        query = "DELETE FROM roles WHERE uuid = ?"
        where = (uuid,)
        # call do_delete method from DBManager
        return self.db_manager.do_delete(query, where, False)   
    
    def role_has_permissions():
        pass


# obj_role = Role()
# print( obj_role.add_role('Pedrito8') )
# rows = obj_role.get_role() 
# for row in rows:
#     print( dict(row) )