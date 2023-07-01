'''
    This file contains the Authorisation Service Class
'''
from dbmanager import DBManager
from permission import Permission

class AuthorisationService:

    def __init__(self):
        # initialise instance of DBManager
        self.db_manager = DBManager()
        self.permission = Permission()
        # a dictionary to store the action-to-permission mappings
        self.action_to_permission = {
            'Add New User': 'create-user'
        }
        
    def check_permissions(self, action, role):
        permission_id = self.action_to_permission[action]
        role_id = role
        values = (permission_id, role_id) 
        query = "SELECT * FROM role_to_permission WHERE pe " # select row where permission id is same as permission id given + role id
        result = self.db_manager.do_select(query, [values])
        if len(result) >= 1:
            return True
        else:
            return False