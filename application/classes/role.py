""" This file contains the Role class and associated methods."""

import os
import sys
import datetime
from dbmanager import DBManager
<<<<<<< HEAD

# Modify search path for module imports:
fpath = os.path.join(os.path.dirname(__file__).rstrip('classes'), 'data')
sys.path.append(fpath)

=======
import uuid
>>>>>>> main

class Role:
    """
    A class for encapsulating all methods which
    interact with the database roles table. 
    """

    def __init__(self, name = ''):
        self._name = name
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
        # Initialise an instance of DBManager (connect to database):
        self.db_manager = DBManager()

<<<<<<< HEAD
    def get_role(self, id):
        # If id is true, retrieve row in roles table:
        if id:
            return self.db_manager.do_select('SELECT * FROM roles \
                                             WHERE id = ?', (id,))
=======
    def get_role(self, uuid):
      
        if uuid:
            return self.db_manager.do_select('SELECT * FROM roles WHERE uuid = ?', (uuid,) )
>>>>>>> main
        else:
            return False
    
    def add_role(self, name):
        # If name is true, create a record in the roles table:
        if name:          
<<<<<<< HEAD
            return self.db_manager.do_insert("INSERT INTO roles(name) \
                                             VALUES (?) ", 
                                             (name,), False)  
        else:
            return False

    def update_role(self, id, name):
        # Update the 'updated_at' attribute with current date/ time:
        self._updated_at = datetime.datetime.now()
        # Perform database query to update name/ updated_ at attributes:
        query = "UPDATE roles SET name='" + name + "', \
            updated_at= " + self._updated_at + " WHERE role_id=?"
        values = (id,)
        # Call the do_update method and update the roles table:
        self.db_manager.do_update(query, values)

    def delete_role(self, id):
        # Query rows to delete from roles table using id attribute:
        query = "DELETE FROM roles WHERE id = ?"
        where = (id,)
        # Call the 'do_delete' method to delete the record:
=======
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
>>>>>>> main
        return self.db_manager.do_delete(query, where, False)   
    
    def role_has_permissions():
        pass


#obj_role = Role()
#print( obj_role.add_role('Pedrito8'))
#rows = obj_role.get_role() 
#for row in rows:
#    print( dict(row))