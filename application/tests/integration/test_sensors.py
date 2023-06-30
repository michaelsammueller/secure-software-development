'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface, GeigerCounter, Thermometer
from mock import MockAuthorisationService, MockLoginService, MockLogger, MockUser
import unittest

class TestThermometer(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for the thermometer.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        self.cli.connect_action_controller(ActionsController())
        self.cli.action_controller.connect_thermometer(Thermometer())

        # mock classes
        self.cli.connect_login_service(MockLoginService())
        self.cli.action_controller.connect_authorisation_service(MockAuthorisationService())
        self.cli.action_controller.connect_logger(MockLogger())
        self.cli.action_controller.connect_user(MockUser())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda: "Hello, test_name!"

    def test_view_temperature(self):
        '''
            A method that tests the view temperature option.
        '''
        mock_selections = (x for x in ['1', '8', 'C', 'Y', '8', 'F', 'Y', '8', 'K', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections) # comment line for demo
        self.assertTrue(self.cli.display_main_menu())

class TestGeigerCounter(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for the thermometer.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        self.cli.connect_action_controller(ActionsController())
        self.cli.action_controller.connect_geiger_counter(GeigerCounter())

        # mock classes
        self.cli.connect_login_service(MockLoginService())
        self.cli.action_controller.connect_authorisation_service(MockAuthorisationService())
        self.cli.action_controller.connect_logger(MockLogger())
        self.cli.action_controller.connect_user(MockUser())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password') # monkey patch
        self.cli.greeting = lambda: "Hello, test_name!" # monkey patch

    def test_view_radiation(self):
        '''
            A method that tests the view temperature option.
        '''
        mock_selections = (x for x in ['1', '9', 'Rem', 'Y', '9', 'SV', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections) # comment line for demo
        self.cli.display_main_menu()

if __name__ == '__main__':
    unittest.main()
