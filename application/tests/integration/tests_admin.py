'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface, DBManager, User, DBShape
from mock import MockAuthorisationService, MockLoginService, MockLogger, MockUserService
import unittest
from random import randint

class TestAdminActions(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for superadmins.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        self.cli.connect_action_controller(ActionsController())

        # mock classes
        login_service = MockLoginService()
        self.cli.connect_login_service(login_service)
        self.cli.action_controller.connect_authorisation_service(MockAuthorisationService())
        self.cli.action_controller.connect_login_service(login_service)
        self.cli.action_controller.connect_logger(MockLogger())
        self.cli.action_controller.connect_user_service(MockUserService())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda x: f"Hello, {x}!"

    def test_add_user(self):
        '''
            A method that tests the add user option.
        '''
        # test selections
        mock_selections = (x for x in ['1', '1', 'test_user', 'astronaut', '01/01/1971', 'USA', 'username', 'password', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

        # test database integration
        db_path = 'application/tests/integration/testdata.db'
        DBShape(db_path)
        user_service = User()
        db_manager = DBManager(db_path)
        user_service.connect_db_manager(db_manager)
        self.cli.action_controller.connect_user_service(user_service)

        mock_selections = (x for x in ['1', '1', 'test_user', 'astronaut', '01/01/1971', 'USA', f'username{randint(0, 2**16)}', 'password', 'Y', '3', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())


    # def test_delete_user(self):
    #     '''
    #         A method that tests the delete user option.
    #     '''
    #     # tests selections
    #     mock_selections = (x for x in ['1', '2', 'test_user', 'N', '2'])
    #     self.cli.ask_for_selection = lambda: next(mock_selections)
    #     self.assertTrue(self.cli.display_main_menu())

    #     # tests database integration
    #     user_service = User()
    #     db_manager = DBManager('testdata.db')
    #     user_service.connect_db_manager(db_manager)
    #     self.cli.action_controller.connect_user_service(user_service)

    #     mock_selections = (x for x in ['1', '2', 'test_user', 'N', '2'])
    #     self.cli.ask_for_selection = lambda: next(mock_selections)
    #     self.assertTrue(self.cli.display_main_menu())

if __name__ == '__main__':
    unittest.main()
