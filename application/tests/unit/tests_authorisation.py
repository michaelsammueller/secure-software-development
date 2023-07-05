'''
    This file contains unit tests for Authorisation class components.
'''
from context import AuthorisationService
import unittest

class TestAuthorisation(unittest.TestCase):
    '''
        A class for encapsulating unit tests for the Authorisation Service class.
    '''
    def setUp(self):
        self.authserv = AuthorisationService()

    def test_get_permission_id(self):
        '''
            A method that tests getting the permission id.
        '''
        self.assertEqual(self.authserv.get_permission_id('Add New User'), '1')
    
if __name__ == '__main__':
    unittest.main()

