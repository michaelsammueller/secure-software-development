'''
    This file contains the Authorisation Service Class
'''
from role import Role
from user import User

class AuthorisationService:

    def __init__(self):
        self.__role = Role()
        self.__user = User()
        # a dictionary to store the action-to-permission_id mappings:
        self.action_to_permission = {
            "Add New User": "create-user",
            "Delete User": "delete-user",
            "Update User": "update-user",
            "Add Health Record": "add-health-record",
            "View Health Record": "view-health-record",
            "Update Health Record": "update-health-record",
            "Delete Health Record": "delete-record",
            "View Temperature": "view-temperature",
            "View Radiation Level": "view-radiation",
        }

    # Return name of role according to role_id:
    def get_role_name(self, id):
        return self.__role.get_role(id)
     
    # Return name of user's role according to username:
    def get_user_role(self, username):
        return self.__user.get_user_role(username)

    # Check if role has permission: 
    def check_permissions(self, action, role_id):
        permission = self.action_to_permission[action]
    
        # select row where permission matches role_id
        query = "SELECT * FROM role_has_permissions WHERE permission_id = ? AND role_id = ?" 
        values = (permission, role_id)

        result = self.db_manager.do_select(query, values)
        if len(result) >= 1:
            return True
        else:
            return False
           
    def connect_db_manager(self, db_manager):
        # connects to the db_manager
        self.db_manager = db_manager
        