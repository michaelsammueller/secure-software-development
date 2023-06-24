'''
    This file contains the Role class.
'''

import sqlite3
from imports import Permission

class Role:
    '''
        A parent class for the system roles.
    '''
    def __init__(self, name, role_id):
        self.name = name
        self.role_id = role_id

    def add_permission(self, permission_id):
        '''
            A method to store the role_id with the corresponding permission_id
            in the table role_has_permissions
        '''
        #connect to SQL databse
        connect = sqlite3.connect('data/securespace.db')
        cursor = connect.cursor()

        #insert role_id and permission_id pairing into the database
        cursor.execute("INSERT INTO role_has_permissions (role_id, permission_id) VALUES (?, ?)",
                       (self.role_id, permission_id))
        
        #commit the change and close the database connection
        connect.commit()
        connect.close()
   
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

