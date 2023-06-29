"""
    This file contains the CommandLineInterface class
"""

# Imports
from imports import getpass, Login_Service, User


# CommandLineInterface class
# This class will be responsible for handling user input
class CommandLineInterface:
    def __init__(self, selection, confirmation, user):
        self.selection = selection
        self.confirmation = confirmation
        self.user = User()  # Will be an instance of the User class

    def greeting(self):
        """Display greeting message"""
        print(f"""
        -------------------------
        Welcome, {self.user.username}!
        -------------------------\n""")

    def get_user_information(self, attribute=None):
        """
            Retrieve user information.
            Args:
                attribute: The attribute to retrieve (e.g. 'first_name')
            Returns:
                The value of the specified attribute. If no attribute is
                specified, all attributes are returned.
        """
        if attribute is None:
            return vars(self.user)
        else:
            return getattr(self.user, attribute)

    def request_login_details(self):
        """Request user login details"""
        username = input("Username: ")
        password = getpass.getpass("Password: ", stream=None)
        return username, password

    def ask_for_selection(self):
        """Request user selection"""
        selection = input("Enter your selection: ")
        return selection

    def ask_for_confirmation(self):
        """Request user confirmation"""
        while True:
            confirmation = input("Enter Y to confirm or N to cancel: ")
            if confirmation.upper() == 'Y':
                return True
            elif confirmation.upper() == 'N':
                return False
            else:
                print("Invalid selection. Please enter 'Y' or 'N'.\n")

    def display_user_menu(self, username):
        """Display user menu options"""
        self.greeting()

        while True:
            pass  # Create an instance of the "Action_Controller" class

    def display_main_menu(self):
        """Display main menu options"""
        while True:
            print("1. Login")
            print("2. Exit\n")

            # Request user selection
            selection = self.ask_for_selection()

            # Handle user selection
            if selection == '1':
                username, password = self.request_login_details()  # Request user login details
                # Create instance of Login_Service class
                login_service = Login_Service(username, password)
                login_service.login()  # Login user
            elif selection == '2':
                print("Exiting...\n")
                break
            else:
                print("Invalid selection.\n")

    # change_password method (SHOULD LIVE IN ACTION CONTROLLER - NOT HERE)
    # Should this method require reauthentication?
    def change_password(self):
        """Changes user password"""
        pass

    # change_phrase method (SHOULD LIVE IN ACTION CONTROLLER - NOT HERE)
    # Should this method require reauthentication?
    def change_phrase(self):
        """Changes user phrase"""
        pass
