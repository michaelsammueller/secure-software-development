'''
    This file contains integration tests for functionality involving loggers.
'''
from context import ActionsController, CommandLineInterface, GeigerCounter, Thermometer, Logger
from mock import MockAuthorisationService, MockLoginService, MockEncryptionService, MockAuditor
import unittest

class TestLoggers(unittest.TestCase):
    '''
        A class for encapsulating functionality tests for the logger.
    '''
    def setUp(self):
        self.cli = CommandLineInterface()
        self.cli.connect_action_controller(ActionsController())
        self.cli.action_controller.connect_thermometer(Thermometer())
        logger = Logger("application/tests/integration/testlogs.txt")
        self.cli.action_controller.connect_logger(logger)

        # mock classes
        login_service = MockLoginService()
        self.cli.connect_login_service(login_service)
        self.cli.action_controller.connect_authorisation_service(MockAuthorisationService())
        self.cli.action_controller.connect_login_service(login_service)
        logger.connect_auditor(MockAuditor())
        logger.connect_encryption_service(MockEncryptionService())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda x: f"Hello, {x}!"

    def test_view_temperature_logs(self):
        '''
            A method that tests the view temperature option.
        '''
        mock_selections = (x for x in ['1', '8', 'C', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

if __name__ == '__main__':
    unittest.main()
