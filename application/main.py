"""
    Contains the main function for the program.
"""
# Imports
from imports import CommandLineInterface, User, ActionsController, Input_Sanitisation_Service, Encryption_Service, Login_Service

# Insert test user

john_doe = User('john doe', '1', '30061998', '1', '1', 'john.doe', b'$2b$12$1sloC3lxVFlrwguDUNmT8O.QAKu6uSxUtyd1EkvsduH7ov9Oyqm.O', 'tryme')

john_doe.add_user()


# Main Function
def main():
    # Create instance of Commandline_Interface class
    commandline_interface = CommandLineInterface()
    login_service = Login_Service()
    action_controller = ActionsController()
    sanitisation_service = Input_Sanitisation_Service()
    encryption_service = Encryption_Service()
    auditor = Auditor(warning_file='warnings.txt', danger_handler='danger.txt')
    logger = Logger(log_file='logs.txt', auditor=auditor, encryption_service=encryption_service)
    commandline_interface.connect_action_controller(action_controller)
    commandline_interface.connect_login_service(login_service)
    commandline_interface.connect_sanitisation_service(sanitisation_service)
    commandline_interface.connect_encryption_service(encryption_service)
    commandline_interface.connect_logger(logger)
    login_service.connect_encryption_service(encryption_service)
    commandline_interface.display_main_menu()

# Run Program
if __name__ == "__main__":
    main()
