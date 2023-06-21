'''
    This file contains the User class.
'''
class User:
    '''
        A class to create user objects.
    '''
    def __init__(self, first_name, last_name, username, password, secret_phrase):
        '''
            attributes come from user
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
            A method to handle system logins by users.
        '''
        pass

    def change_password(self, new_password):
        '''
            A method to handle user password changes.
        '''
        pass

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
