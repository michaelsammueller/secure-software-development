'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface, Logger, GeigerCounter, Thermometer, Input_Sanitisation_Service, Encryption_Service
from mock import MockAuthorisationService, MockLoginService, MockAuditor
import unittest

class TestSensors(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for the thermometer.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        action_controller = ActionsController()
        self.cli.connect_action_controller(action_controller)
        action_controller.connect_thermometer(Thermometer())
        action_controller.connect_geiger_counter(GeigerCounter())
        self.log_path = "application/tests/integration/testlogs.txt"
        logger = Logger(self.log_path)
        self.cli.connect_logger(logger)
        action_controller.connect_logger(logger)
        self.cli.connect_sanitisation_service(Input_Sanitisation_Service())

        # mock classes
        login_service = MockLoginService()
        self.cli.connect_login_service(login_service)
        action_controller.connect_login_service(login_service)
        action_controller.connect_authorisation_service(MockAuthorisationService())
        logger.connect_auditor(MockAuditor())
        logger.connect_encryption_service(Encryption_Service())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda x: f"Hello, {x}!"

    def test_view_temperature(self):
        '''
            A method that tests the view temperature option.
        '''
        mock_selections = (x for x in ['1', '11', 'C', 'Y', 'Y', '11', 'F', 'Y', 'Y', '11', 'K', 'Y', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections) # comment line for demo
        self.assertTrue(self.cli.display_main_menu())

    def test_view_radiation(self):
        '''
            A method that tests the view radiation level option.
        '''
        mock_selections = (x for x in ['1', '12', 'Rem', 'Y', '12', 'SV', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections) # comment line for demo
        self.cli.display_main_menu()

if __name__ == '__main__':
    unittest.main()
