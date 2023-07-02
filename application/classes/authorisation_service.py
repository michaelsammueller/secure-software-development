'''
    This file contains the Authorisation Service Class
'''
class AuthorisationService:

    def __init__(self):
        # a dictionary to store the action-to-permission mappings
        self.action_to_permission = {
            'Add New User': 'create-user'
        }

    def get_permission_id(self, action):
        return self.action_to_permission[action]
        
    def check_permissions(self, action, role):
        permission_id = self.action_to_permission[action]
        role_id = role
        values = (permission_id, role_id) 
        query = "SELECT * FROM role_to_permission WHERE permission_id=?, role_id=?" # select row where permission id is same as permission id given + role id
        result = self.db_manager.do_select(query, [values])
        if len(result) >= 1:
            return True
        else:
            return False
        
    def connect_db_manager(self, db_manager):
        """Connects the db_manager"""
        self.db_manager = db_manager