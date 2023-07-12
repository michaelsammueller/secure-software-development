'''
    This file contains the Authorisation Service Class
'''
class AuthorisationService:

    def __init__(self):
        # a dictionary to store the action-to-permission_id mappings:
        self.action_to_permission = {
            "Add New User": "create-user",
            "Delete User": "delete-user",
            "View All Users": "view-all-users",
            "View User Details": "view-user-details",
            "Update User Details": "update-user-details",
            "Add Health Record": "add-health-record",
            "View User Health Records": "view-user-health-records",
            "Delete User Health Records": "delete-user-health-records",
            "View Temperature": "view-temperature",
            "View Radiation Level": "view-radiation",
        }

    def get_user_role(self, username):
        '''
            Get the role of a user from the database
        '''
        return self.__user_service.get_user_role(username)

    # Check if role has permission: 
    def check_permission(self, action, user_role):
        permission = self.action_to_permission[action]
        permission_id = self.__permission_service.get_permission_id(permission)
        role_id = self.__role_service.get_role_id(user_role)
    
        # select row where permission matches role_id
        query = "SELECT * FROM role_has_permissions WHERE permission_id = ? AND role_id = ?" 
        values = (permission_id, role_id)

        result = self.__db_manager.do_select(query, values)
        if len(result) >= 1:
            return True
        else:
            return False
           
    def connect_db_manager(self, db_manager):
        '''
            Connects to the database manager
        '''
        self.__db_manager = db_manager

    def connect_permission_service(self, permission_service):
        '''
            Connects to the permission_service
        '''
        self.__permission_service = permission_service

    def connect_user_service(self, user_service):
        '''
            Connects to the user_service
        '''
        self.__user_service = user_service

    def connect_role_service(self, role_service):
        '''
            Connects to the role_service
        '''
        self.__role_service = role_service


        