'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface
from mock import MockAuthorisationService, MockHealthRecordService, MockLoginService, MockLogger, MockUser
import unittest

class TestAdminActions(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for superadmins.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        self.cli.connect_action_controller(ActionsController())

        # mock classes
        self.cli.connect_login_service(MockLoginService())
        self.cli.action_controller.connect_authorisation_service(MockAuthorisationService())
        self.cli.action_controller.connect_logger(MockLogger())
        self.cli.action_controller.connect_user(MockUser())
        self.cli.action_controller.connect_health_record_service(MockHealthRecordService())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda: "Hello, test_name!"

    def test_add_health_record(self):
        '''
            A method that tests the add user option.
        '''
        mock_selections = (x for x in ['1', '4', 'test_user', '180', '80', '90', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

if __name__ == '__main__':
    unittest.main()
