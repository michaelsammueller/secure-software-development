'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface, DBManager, User, DBShape, Logger, Encryption_Service, Input_Sanitisation_Service
from mock import MockAuthorisationService, MockLoginService, MockAuditor, MockRoleService

import unittest
from random import randint
import os

class TestAdminActions(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for superadmins.
    '''
    def setUp(self):
        # set up services
        self.cli = CommandLineInterface()
        self.cli.connect_sanitisation_service(Input_Sanitisation_Service())
        action_controller = ActionsController()
        self.cli.connect_action_controller(action_controller)
        self.log_path = 'application/tests/integration/testlogs.txt'
        logger = Logger(self.log_path)
        self.cli.connect_logger(logger)
        action_controller.connect_logger(logger)
        logger.connect_encryption_service(Encryption_Service())
        self.db_path = 'application/tests/integration/testdata.db'
        if not os.path.exists(self.db_path):
            DBShape(self.db_path)
        self.db_manager = DBManager(self.db_path)
        user = User()
        user.connect_role_service(MockRoleService())
        action_controller.connect_user_service(user)
        user.connect_db_manager(self.db_manager)

        # mock classes
        login_service = MockLoginService()
        self.cli.connect_login_service(login_service)
        action_controller.connect_login_service(login_service)
        action_controller.connect_authorisation_service(MockAuthorisationService())
        logger.connect_auditor(MockAuditor())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda x: f"Hello, {x}!"

    def test_add_user(self):
        '''
            A method that tests the add user option.
        '''

        print("----Adding user----")
        # test database and logger integration
        mock_selections = (x for x in ['1', '1', 'test_user', 'astronaut', '01-01-1971', 'US', f'username{randint(0, 2**16)}', 'password', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

    def test_view_all_users(self):
        '''
            A method that tests the view users option.
        '''

        print("----Viewing All Users----")
        # test database and logger integration
        mock_selections = (x for x in ['1', '3', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

    def test_view_user(self):
        '''
            A method that tests the view user option.
        '''

        print("----Viewing One User----")
        # test database and logger integration
        mock_selections = (x for x in ['1', '4', 'd4b259', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

    def test_delete_user(self):
        '''
            A method that tests the delete user option.
        '''

        print("----Deleting a user----")
        # test database and logger integration
        mock_selections = (x for x in ['1', '4', '5a08d606-8ed8-434d-8928-e50913ee7134', 'Y', '2', '5a08d606-8ed8-434d-8928-e50913ee7134', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

    def test_update_user(self):
        '''
            A method that tests the update user information option.
        '''

        print("----Updating a user----")
        # test database and logger integration
        mock_selections = (x for x in ['1', '5', '77432281-1a57-4de2-83c8-57d5e1997287', 'role', 'Astronaut', 'Y', '4', '77432281-1a57-4de2-83c8-57d5e1997287', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

if __name__ == '__main__':
    unittest.main()
