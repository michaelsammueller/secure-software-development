'''
    This file contains the Role class.
'''
from dbmanager import DBManager
import datetime

class Role:
    '''
        A parent class for the system roles.
    '''

    def __init__(self):
        # need id
        self._name = ""       
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
        # initialise instance of DBManager
        self.db_manager = DBManager   


    def get_role(self, id):
        if id:
            return self.db_manager.do_select('SELECT * FROM roles WHERE id = ?', (id,) )
        else:
            return False

    # Creates a record and returns the inserted id
    def add_role(self, name):        
        if name:
            return self.db_manager.do_insert("INSERT INTO roles(name) VALUES (?) ", (name,),  False )  
        else:
            return False

    def update_role(self, id, name):
        # update the 'updated_at' attribute.
        self._updated_at = datetime.datetime.now()
        # perform database query to update permission attributes.
        query = "UPDATE roles SET name='" + name + "', updated_at= " + self._updated_at + " WHERE role_id=?"
        values = (id,)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_role(self, id):
        # identify records to delete with id
        query = "DELETE FROM roles WHERE id = ?"
        where = (id,)
        # call do_delete method from DBManager
        return self.db_manager.do_delete(query, where, False)
       
    
    def role_has_permissions():
        pass