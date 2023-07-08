'''
    This file contains the User class.
'''
import uuid

class User:
    '''
        A class to create user objects.
    '''

    def add_user(self, user_details):
        '''
            Adds a user to the database
        '''
        # perform database query to save user attributes.
        query = "INSERT INTO users (uuid, name, code, dob, role_id, \
            country_id, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        values = (str(uuid.uuid4()), user_details['name'], user_details['username'], user_details['date of birth'], user_details['role'],
                  user_details['country of employment'], user_details['username'], user_details['password'])

        # call do_insert method from DBmanager.
        return self.__db_manager.do_insert(query, values, dry=False)

    def view_all_users(self):
        '''
            View users from the database
        '''
        query = "SELECT username, uuid FROM users"
        where = ()

        # call do_select method from DBManager.
        result = self.__db_manager.do_select(query, where)
        json = {row[0] : row[1] for row in result}
        return json
    
    
    def view_user(self, uuid):
        '''
            View a user from the database
        '''
        query = "SELECT * FROM users WHERE uuid = ?"
        where = (uuid,)

        # call do_select method from DBManager.
        result = self.__db_manager.do_select(query, where)
        json = {result.keys()[i] : value for i, value in enumerate(result)}
        return json
    
    def delete_user(self, name): #TODO name or uuid
        '''
            Delete a user from the database
        '''
        query = "DELETE FROM roles WHERE name = ?"
        where = (name,)
        # call do_delete method from DBManager
        return self.__db_manager.do_delete(query, where, False)   

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.__db_manager = db_manager

