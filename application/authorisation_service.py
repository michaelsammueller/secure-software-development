'''
    This file contains the Authorisation Service Class
'''

import sqlite3

class AuthorisationService:
    '''
        A class to initialise a connection to the database to authorise
        roles and permissions
    '''
    def __init__(self, db_path='data/securespace.db'):
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()

def role_has_permission(self, role_id, permission_id):
    '''
        A method to check if there is a match between the role_id and 
        permission_id
    '''
    query = '''
        SELECT COUNT(*) FROM role_has_permissions
        WHERE role_id = ? AND permission_id = ?
    '''
    self.cursor.execute(query, (role_id, permission_id))
    count = self.cursor.fetchone()[0]
    return count > 0

def __del__(self):
    '''
        A method to clean up and close the database connection
    '''
    self.cursor.close()
    self.connect.close()

def make_poll(self):
    pass
