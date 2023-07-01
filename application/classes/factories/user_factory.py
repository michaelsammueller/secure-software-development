'''
    This file contains the Thermometer class.
'''
from classes.factories.abstract import Factory
from classes.models.user import User


class UserFactory(Factory):
    '''
        A class for encapsulating a thermometer component.
    '''
    def __init__(self):
        self.model = User
        self.users = {}

    def __getitem__(self, username):
        return self.get({'username' : username})
    
    def create(self, user_details):
        '''
            A method for creating a user.
        '''
        # create user
        new_user = self.model(user_details)
        # connect user to services
        new_user.connect_db_manager(self.db_manager)
        new_user.connect_role_service(self.role_service)
        new_user.connect_country_service(self.country_service)
        # store user
        username = user_details['username']
        self.users[username] = new_user
        # return user
        return new_user
    
    def get(self, user_details):
        '''
            A method for getting a user.
        '''
        if 'username'in user_details:
            username = user_details['username']
            return self.users[username]
        else:
            return None
    
    def connect_db_manager(self, db_manager):
        '''
            A method for connecting the database manager.
        '''
        self.db_manager = db_manager

    def connect_role_service(self, role_service):
        '''
            A method for connecting the role service.
        '''
        self.role_service = role_service

    def connect_country_service(self, country_service):
        '''
            A method for connecting the country service.
        '''
        self.country_service = country_service
