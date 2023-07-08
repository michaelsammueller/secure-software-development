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
    
    def get_user_role(self, *args, **kwargs):
        '''
        A method for mocking a user role.
        '''
        return "developer"
    
class MockLogger:
    '''
        A class for mocking the logger.
    '''
    def log(self, *args, **kwargs):
        '''
        A method for mocking logging.
        '''
        return True
    
class MockAuditor:
    '''
        A class for mocking the logger.
    '''
    def audit(self, *args, **kwargs):
        '''
        A method for mocking logging.
        '''
        return False

class MockLoginService:
    '''
        A class for mocking the login service.
    '''
    def login(self, *args, **kwargs):
        '''
        A method for mocking a login.
        '''
        return True
    
    def get_loggedin_username(self, *args, **kwargs):
        '''
        A method for mocking a username.
        '''
        return "Brad"
    
class MockEncryptionService:
    '''
        A class for mocking the encryption service.
    '''
    def encrypt(self, *args, **kwargs):
        '''
        A method for mocking a login.
        '''
        return "ENCRYPTED"
    
class MockUserService:
    '''
        A class for mocking a user.
    '''
    
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