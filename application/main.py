"""
    Contains the main function for the program.
"""
# Imports
from imports import AuthSeeder, DBShape, DBManager, CommandLineInterface, ActionsController, Input_Sanitisation_Service, Encryption_Service, Login_Service, Logger
from imports import Thermometer, GeigerCounter, User, Role, Permission, HealthRecord, Country
from tests.integration.mock import MockAuditor, MockLoginService, MockAuthorisationService

# Insert test user

# john_doe = User('john doe', '1', '30061998', '1', '1', 'john.doe', b'$2b$12$1sloC3lxVFlrwguDUNmT8O.QAKu6uSxUtyd1EkvsduH7ov9Oyqm.O', 'tryme')

# john_doe.add_user()


# Main Function
def main():
    # Create services
    commandline_interface = CommandLineInterface()
    login_service = MockLoginService()
    action_controller = ActionsController()
    sanitisation_service = Input_Sanitisation_Service()
    encryption_service = Encryption_Service()
    authorisation_service = MockAuthorisationService
    log_path = 'application/logs.txt'
    logger = Logger(log_path)
    auditor = MockAuditor()
    authseeder = AuthSeeder()
    db_path = 'application/data.db'
    DBShape(db_path)
    db_manager = DBManager(db_path)
    thermometer = Thermometer()
    geiger_counter = GeigerCounter()
    user = User()
    role = Role()
    permission = Permission()
    health_record = HealthRecord()
    country = Country()
    # connect services
    commandline_interface.connect_action_controller(action_controller)
    commandline_interface.connect_login_service(login_service)
    commandline_interface.connect_sanitisation_service(sanitisation_service)
    commandline_interface.connect_encryption_service(encryption_service)
    commandline_interface.connect_logger(logger)

    action_controller.connect_login_service(login_service)
    action_controller.connect_authorisation_service(authorisation_service)
    action_controller.connect_logger(logger)
    action_controller.connect_user_service(user)
    action_controller.connect_thermometer(thermometer)
    action_controller.connect_geiger_counter(geiger_counter)
    action_controller.connect_health_record_service(health_record)

    sanitisation_service.connect_logger(logger)
    logger.connect_auditor(auditor)
    logger.connect_encryption_service(encryption_service)
    country.connect_db_manager(db_manager)
    role.connect_db_manager(db_manager)
    permission.connect_db_manager(db_manager)
    user.connect_db_manager(db_manager)
    health_record.connect_db_manager(db_manager)

    authseeder.connect_country(country)
    authseeder.connect_role(role)
    authseeder.connect_permission(permission)

    commandline_interface.display_main_menu()

# Run Program
if __name__ == "__main__":
    main()
