'''
    This file contains the Role class.
'''

class Role:
    '''
        A parent class for the system roles.
    '''
    def __init__(self, name, role_id):
        self.name = name
        self.role_id = role_id

    def role_has_permission(self, permission_id):
        '''
        A method which pairs the role_id with the permission_id
        '''
        if self.role_id == permission_id:
            return True
        else:
            return False
   
class Astronaut(Role):
    '''
        A child class for the 'Astronaut' role.
    '''
    def __init__(self):
        super().__init__("Astronaut")
        self.role_id = int

    def __str__(self):
        return f"{self.name} has {self.role_id} role id"
        
class Moderator(Role):
    '''
        A child class for the 'Moderator' role.
    '''
    def __init__(self):
        super().__init__("Moderator")
        self.role_id = int

    def __str__(self):
        return f"{self.name} has {self.role_id} role id"

class Superadmin(Role):
    '''
        A child class for the 'Superadmin' role.
    '''
    def __init__(self):
        super().__init__("Superadmin")
        self.role_id = int

    def __str__(self):
        return f"{self.name} has {self.role_id} role id"
