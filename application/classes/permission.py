'''
    This file contains the Permission class.
'''
import os
import sys
import datetime
fpath = os.path.join(os.path.dirname(__file__).rstrip('classes'), 'data')
#print(fpath)
sys.path.append(fpath)
from dbmanager import DBManager


class Permission:
    '''
        A parent class for the system permissions.
    '''

    def __init__(self, name = ''):
        # need id
        self._name = name       
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
        # initialise instance of DBManager
        self.db_manager = DBManager()

    def get_permission(self, id):
      
        if id:
            return self.db_manager.do_select('SELECT * FROM permissions WHERE id = ?', (id,) )
        else:
            return False
    
    # Creates a record and returns the inserted id
    def add_permission(self, name):        
        if name:          
            return self.db_manager.do_insert("INSERT INTO permissions(name) VALUES (?) ", (name,),  False )  
        else:
            return False

    def update_permission(self, id, name):
        # update the 'updated_at' attribute.
        self._updated_at = datetime.datetime.now()
        # perform database query to update permission attributes.
        query = "UPDATE permissions SET name='" + name + "', updated_at= " + self._updated_at + " WHERE permission_id=?"
        values = (id,)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_permission(self, id):
        # identify records to delete with id
        query = "DELETE FROM permissions WHERE id = ?"
        where = (id,)
        # call do_delete method from DBManager
        return self.db_manager.do_delete(query, where, False)   
   

obj_permission = Permission()
print( obj_permission.add_permission('approve-accounts') )
# rows = obj_permission.get_permission() 
# for row in rows:
#     print( dict(row) )