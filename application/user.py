'''
    This file contains the User class.
'''
import sqlite3
from imports import Login_Service

class User:
    '''
        A class to create user objects.
    '''
    def __init__(self, first_name, last_name, username, password, secret_phrase):
        '''
            attributes come from user set-up
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.secret_phrase = secret_phrase
        '''
            attribute retrieved from logger
        '''
        self.last_login = str
    
    def login(self):
        '''
            A method to handle user logins
        '''
        #create an instance of Login_Service
        login_service = Login_Service()

        #call authenticate_user_credentials method
        is_authenticated = login_service.authenticate_user_credentials(self.username, self.password)

        #check authentication
        if is_authenticated:
            print("Successful login")
        else:
            print("Invalid login")

    def change_password(self, new_password):
        '''
            A method to handle user password changes.
        '''
        #update the password in the User object
        self.password = new_password

        #update the password in the database
        db = sqlite3.connect('data/securespace.db')
        cursor = db.cursor()

        query = "UPDATE users SET password = ? WHERE username = ?"
        cursor.execute(query, (new_password, self.username))

        db.commit()
        db.close()

    def change_phrase(self, new_phrase):
        '''
            A method to handle user secret phrase changes.
        '''
        pass

    def is_phrase_required(time):
        '''
            A method for...
        '''
        pass

    def decrypt(secret_phrase):
        '''
            A method for...
        '''
        pass

            A method for...
        '''
        pass
