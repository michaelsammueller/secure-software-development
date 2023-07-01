'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface
from mock import MockAuthorisationService, MockLoginService, MockLogger, MockUser, MockUserFactory
import unittest

class TestAdminActions(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for the thermometer.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        self.cli.connect_action_controller(ActionsController())

        # mock classes
        self.cli.connect_login_service(MockLoginService())
        self.cli.action_controller.connect_authorisation_service(MockAuthorisationService())
        self.cli.action_controller.connect_logger(MockLogger())
        self.cli.action_controller.connect_user(MockUser())
        self.cli.action_controller.connect_user_factory(MockUserFactory())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda: "Hello, test_name!"

    def test_add_user(self):
        '''
            A method that tests the add user option.
        '''
        mock_selections = (x for x in ['1', '1', 'test_user', 'astronaut', '01/01/1971', 'USA', 'username', 'password', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

    def test_delete_user(self):
        '''
            A method that tests the delete user option.
        '''
        mock_selections = (x for x in ['1', '2', 'test_user', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

if __name__ == '__main__':
    unittest.main()
