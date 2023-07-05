'''
    This is a file that contains classes with mock methods for testing.
'''

class MockAuthorisationService:
    '''
        A class for mocking the authorisation service.
    '''
    def check_permission(self, *args, **kwargs):
        '''
        A method for mocking authorisation.
        '''
        return True
    
class MockLogger:
    '''
        A class for mocking the logger.
    '''
    def log(self, *args, **kwargs):
        '''
        A method for mocking logging.
        '''
        return True

class MockLoginService:
    '''
        A class for mocking the login service.
    '''
    def login(self, *args, **kwargs):
        '''
        A method for mocking a login.
        '''
        return True
    
class MockUserService:
    '''
        A class for mocking a user.
    '''

    def get_name(self, *args, **kwargs):
        '''
        A method for mocking a user name.
        '''
        return "Brad"

    def get_role(self, *args, **kwargs):
        '''
        A method for mocking a user role.
        '''
        return "developer"
    
    def add_user(self, *args, **kwargs):
        '''
        A method for mocking adding a user.
        '''
        return True
    
    def delete_user(self, *args, **kwargs):
        '''
        A method for mocking deleting a user.
        '''
        return True
    
class MockHealthRecordService:
    '''
        A class for mocking the health record service.
    '''
    def add_record(self, *args, **kwargs):
        '''
        A method for mocking a login.
        '''
        return True