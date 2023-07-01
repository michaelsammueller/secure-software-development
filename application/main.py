"""
    Contains the main function for the program.
"""
# Imports
from commandline_interface import CommandLineInterface
from user import User
from login_service import Login_Service
from classes.controllers.actionscontroller import ActionsController
from input_sanitisation import Input_Sanitisation_Service
from encryption_service import Encryption_Service

# Insert test user
"""
john_doe = User('john doe', '1', '30061998', '1', '1', 'john.doe', b'$2b$12$1sloC3lxVFlrwguDUNmT8O.QAKu6uSxUtyd1EkvsduH7ov9Oyqm.O', 'tryme')

john_doe.add_user()
"""

# Main Function
def main():
    # Create instance of Commandline_Interface class
    commandline_interface = CommandLineInterface()
    login_service = Login_Service()
    action_controller = ActionsController()
    sanitisation_service = Input_Sanitisation_Service()
    encryption_service = Encryption_Service()
    commandline_interface.connect_action_controller(action_controller)
    commandline_interface.connect_login_service(login_service)
    commandline_interface.connect_sanitisation_service(sanitisation_service)
    commandline_interface.connect_encryption_service(encryption_service)
    commandline_interface.display_main_menu()

# Run Program
if __name__ == "__main__":
    main()
