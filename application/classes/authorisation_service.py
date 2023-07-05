'''
    This file contains the Authorisation Service Class
'''

class AuthorisationService:

    def __init__(self):
        # a dictionary to store the action-to-permission_id mappings
        self.action_to_permission = {
            "Add New User": "create-user",
            "Delete User": "delete-user",
            "Add Health Record": "add-health-record",
            "View Health Record": "view-health-record",
            "View Warning Logs": "view-warning-log",
            "View Temperature": "view-temperature",
            "View Radiation Level": "view-radiation",
            "Update Health Record": "update-health-record",
            "Delete Health Record": "delete-record"
        }
        
    def check_permissions(self, action, role_id):
        permission = self.action_to_permission[action]
    
        # select row where permission matches role id
        query = "SELECT * FROM role_to_permission WHERE permission = ? AND role_id = ?" 
        values = (permission, role_id)

        result = self.db_manager.do_select(query, [values])
        if len(result) >= 1:
            return True
        else:
            return False
        
    def connect_db_manager(self, db_manager):
        # connects to the db_manager
        self.db_manager = db_manager
        
