'''
    This file contains the Role class.
'''
from dbmanager import DBManager
import time

class Role:
    '''
        A parent class for the system roles.
    '''

    def __init__(self):
        # need id
        self._name = ""       
        self._created_at = int(time.time()) 
        self._updated_at = int(time.time()) 
        # initialise instance of DBManager
        self.db_manager = DBManager   


    def get_role(self, id):
        return self.db_manager.do_select('SELECT * FROM roles WHERE id = ?', (id,) )

    def add_role(self):
        # update created_at and updated_at attributes        
        self._created_at = int(time.time()) 
        self._updated_at = int(time.time()) 

        # prepare the data for updating the role table
        values = (self._name, self._created_at, self._updated_at)

        # call do_insert method from DBManager
        query = """INSERT INTO roles (name, created_at, updated_at) 
                   VALUES (?, ?, ?)"""
        self.db_manager.do_insert(query, [values], dry=False)

    def update_role(self, id):
        # update the 'updated_at' attribute.
        self._updated_at = self.current_time

        # perform database query to update permission attributes.
        query = "UPDATE roles SET name=?, updated_at=? WHERE role_id=?"
        values = (id)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_role(self):
        # identify records to delete with id
        query = "DELETE FROM roles WHERE id = ?"
        where = (self._role_id)

        # call do_delete method from DBManager
        result = self.db_manager.do_delete(query, where, dry=True)
        
        # if id is matched, records will be deleted.
        if result:
            print(f"Deleted {len(result)} record(s) from roles table.")
            return True
        
        # if id is not matched, records will not be deleted.
        else:
            print("No records deleted.")
            return False
    
    def role_has_permissions():
        pass
