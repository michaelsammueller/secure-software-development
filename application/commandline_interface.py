# Imports
from imports import getpass
from imports import Login_Service


# CommandLineInterface class
# This class will be responsible for handling user input
class CommandLineInterface:
    def __init__(self, selection, confirmation, user):
        self.selection = selection
        self.confirmation = confirmation
        self.user = user  # Will be an instance of the User class

    def greeting(self):
        """Display greeting message"""
        print(f"""
        -------------------------
        Welcome, {self.user.username}!
        -------------------------\n""")

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
            pass  # Add options to add health record, view health records, and logout

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
                # If user credentials are valid, display user menu
                if login_service.authenticate_user_credentials(username, password):
                    self.display_user_menu(username)  # Display user menu for logged in user
                else:
                    print("Invalid username or password.\n")
            elif selection == '2':
                print("Exiting...\n")
                break
            else:
                print("Invalid selection.\n")
