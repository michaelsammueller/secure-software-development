'''
    This file contains integration tests for functionality involving sensor components.
'''
from context import ActionsController, CommandLineInterface, DBManager, User, HealthRecord, DBShape, Logger
from mock import MockAuthorisationService, MockLoginService, MockAuditor, MockEncryptionService

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
        action_controller = ActionsController()
        self.cli.connect_action_controller(action_controller)
        self.log_path = 'application/tests/integration/testlogs.txt'
        logger = Logger(self.log_path)
        self.cli.connect_logger(logger)
        action_controller.connect_logger(logger)
        self.db_path = 'application/tests/integration/testdata.db'
        if not os.path.exists(self.db_path):
            DBShape(self.db_path)
        self.db_manager = DBManager(self.db_path)
        user = User()
        action_controller.connect_user_service(user)
        user.connect_db_manager(self.db_manager)
        health_record = HealthRecord()
        action_controller.connect_health_record_service(health_record)
        health_record.connect_db_manager(self.db_manager)

        # mock classes
        login_service = MockLoginService()
        self.cli.connect_login_service(login_service)
        action_controller.connect_login_service(login_service)
        action_controller.connect_authorisation_service(MockAuthorisationService())
        logger.connect_auditor(MockAuditor())
        logger.connect_encryption_service(MockEncryptionService())

        # monkey patches
        self.cli.request_login_details = lambda: ('test_name', 'test_password')
        self.cli.greeting = lambda x: f"Hello, {x}!"

    def test_add_health_record(self):
        '''
            A method that tests the add user option.
        '''

        print("----Adding user----")
        # test database and logger integration
        mock_selections = (x for x in ['1', '5', '5a08d606-8ed8-434d-8928-e50913ee7134', 'headache', '170', '80', '100', 'N', '2'])
        self.cli.ask_for_selection = lambda: next(mock_selections)
        self.assertTrue(self.cli.display_main_menu())

if __name__ == '__main__':
    unittest.main()

