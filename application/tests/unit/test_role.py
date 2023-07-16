'''
    This file contains unit tests for Role class components.
'''
from context import Role
import unittest


class TestRole(unittest.TestCase):
    '''
        A class for encapsulating unit tests for the Role class.
    '''
    def setUp(self):
        self.role = Role()

    def test_get_role(self):
        '''
            A method that tests getting the role.
        '''
        self.assertEqual(self.role.get_role('1'), ('Superadmin'))


if __name__ == '__main__':
    unittest.main()
