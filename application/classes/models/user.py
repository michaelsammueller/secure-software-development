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
        if 'uuid' in user_details.keys():
            _uuid = user_details['uuid']
        else:
            _uuid = str(uuid.uuid4())
        values = (_uuid, user_details['name'], user_details['username'], user_details['date of birth'], user_details['role'],
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
        if result:
            json = {row[0] : row[1] for row in result}
        else:
            json = {}
        return json
    
    
    def view_user(self, user_identifiers):
        '''
            View a user from the database
        '''
        query = "SELECT * FROM users WHERE uuid = ?"
        where = (user_identifiers['uuid'],)

        # call do_select method from DBManager.
        result = self.__db_manager.do_select(query, where)
        if result:
            json = {result[0].keys()[i] : value for i, value in enumerate(result[0])}
            # clean up json
            json['role'] = self.__role_service.get_role_name(json['role_id'])
            del json['role_id']
        else:
            json = {}
        return json
    
    def delete_user(self, user_identifiers):
        '''
            Delete a user from the database
        '''
        query = "DELETE FROM users WHERE uuid = ?"
        where = (user_identifiers['uuid'],)
        # call do_delete method from DBManager
        return self.__db_manager.do_delete(query, where, False)

    def update_user(self, user_information):
        '''
            Update a user from the database
        '''
        field = user_information['field']
        value = user_information['new value']
        if field == 'date of birth':
            field = 'dob'
        elif field == 'country of employment':
            field = 'country_id'
        elif field == 'role':
            field = 'role_id'
            value = self.__role_service.get_role_id(value)
        query = f"UPDATE users SET {field} = {value} WHERE uuid = ?"
        where = (user_information['uuid'],)
        # call do_delete method from DBManager
        return self.__db_manager.do_update(query, where, False)    
    
    def get_user_role(self, username):
        '''
            Get the role of a user from the database
        '''
        query ='SELECT role_id FROM users WHERE username = ?'
        where = (username, )
        role_id = self.__db_manager.do_select(query, where)[0][0]
        return self.__role_service.get_role_name(role_id)

    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.__db_manager = db_manager

    def connect_role_service(self, role_service):
        '''
            A method for connecting the role service.
        '''
        self.__role_service = role_service

