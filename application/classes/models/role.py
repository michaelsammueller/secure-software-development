'''
    This file contains the Role class.
'''
# Imports
import uuid


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
            return self.__db_manager.do_insert("INSERT INTO roles(uuid, name) VALUES (?, ?) ",
                                               (str(uuid.uuid4()), name,),  False)
        else:
            return False

    def delete_role(self, name):
        '''
            Delete a role from the database
        '''
        query = "DELETE FROM roles WHERE id = ?"
        where = (name,)
        # call do_delete method from DBManager
        return self.__db_manager.do_delete(query, where, False)

    def get_role_name(self, role_id):
        '''
            Get the role of a user from the database
        '''
        query = 'SELECT name FROM roles WHERE id = ?'
        where = (role_id, )
        return self.__db_manager.do_select(query, where)[0][0]

    def get_role_id(self, role_name):
        '''
            Get the role of a user from the database
        '''
        query = 'SELECT id FROM roles WHERE name = ?'
        where = (role_name, )
        return self.__db_manager.do_select(query, where)[0][0]

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.__db_manager = db_manager
