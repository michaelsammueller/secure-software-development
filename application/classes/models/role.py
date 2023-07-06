'''
    This file contains the Role class.
'''
import datetime
import time

class Role:
    '''
        A parent class for the system roles.
    '''
    
    # Creates a record and returns the inserted id
    def add_role(self, name):
        '''
            Add a new role to the database
        '''        
        if name:          
            return self.db_manager.do_insert("INSERT INTO roles(name) VALUES (?) ", (name,),  False )  
        else:
            return False

    def delete_role(self, name):
        '''
            Delete a role from the database
        '''
        query = "DELETE FROM roles WHERE id = ?"
        where = (name,)
        # call do_delete method from DBManager
        return self.db_manager.do_delete(query, where, False)   
    

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.db_manager = db_manager


# obj_role = Role()
# print( obj_role.add_role('Pedrito8') )
# rows = obj_role.get_role() 
# for row in rows:
#     print( dict(row) )