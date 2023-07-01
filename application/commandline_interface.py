"""
    This file contains the CommandLineInterface class
"""

# Imports
import getpass
# from imports import getpass, Login_Service, User, Input_Sanitisation_Service

# CommandLineInterface class
# This class will be responsible for handling user input
class CommandLineInterface:
    #def __init__(self, selection, confirmation, user):
        #self.selection = selection
        #self.confirmation = confirmation
        #self.user = User()  # Will be an instance of the User class

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
        print("\n")
        return selection

    def ask_for_confirmation(self):
        """Request user confirmation"""
        while True:
            print("Enter Y to confirm or N to cancel.")
            confirmation = self.ask_for_selection()
            if confirmation.upper() == 'Y':
                return True
            elif confirmation.upper() == 'N':
                return False
            else:
                print("Invalid selection. Please enter 'Y' or 'N'.\n")

    def display_user_menu(self):
        """Display user menu options"""
        self.greeting()
        while True:
            options = self.action_controller.get_actions()
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
        
            # Request user selection
            selection = self.ask_for_selection()
            # Handle user selection
            try:
                selection = int(selection)
            except:
                print("Invalid selection.\n")
                continue
            if selection <= len(options):
                # Get additional paramaters from user 
                params = self.action_controller.get_action_params(options[selection - 1])
                details = {}
                print("\nRequesting details...")
                for param in params:
                    if not param[1]: # only field name provided
                        print(f"{param[0]}")
                        details[param[0]] = self.ask_for_selection()
                    else: # field name and options provided
                        print(f"\nOptions for {param[0]}: {param[1]}")
                        details[param[0]] = self.ask_for_selection()
                # Perform action
                results = self.action_controller(options[selection - 1], details)
                print("\nResults...")
                print(f"{[f'{key}: {value}' for key, value in results.items()]}")
                # Ask to continue
                print("\nWould you like to continue?")
                if self.ask_for_confirmation():
                    continue
                else:
                    break
            else:
                print("Invalid selection.\n")

    def display_main_menu(self):
        """Display main menu options"""
        while True:
            print("\n1. Login")
            print("2. Exit\n")

            # Request user selection
            selection = self.ask_for_selection()

            # Handle user selection
            if selection == '1':
                username, password = self.request_login_details()  # Request user login details
                # Handle Login
                if self.login_service.login(username, password):
                    self.display_user_menu()
                else:
                    print("Unable to login.\n")
            elif selection == '2':
                # Handle Exit
                print("Exiting...\n")
                return True # Confirms exit
            else:
                print("Invalid selection.\n")

    # Will live in here for now
    def change_password(self):
        """Changes user password"""
        # Ask user for reauthentication
        username, password = self.request_login_details()
        # Create instance of Login_Service class
        login_service = Login_Service(username, password)
        # Authenticate user credentials
        if login_service.authenticate_user_credentials():
            # Ask user for new password
            new_password = getpass.getpass("New Password: ", stream=None)
            # Ask user to confirm new password
            new_password_confirmation = getpass.getpass("Confirm New Password: ", stream=None)
            # Check if new password matches confirmation
            if new_password == new_password_confirmation:
                # Sanitise password
                new_password = Input_Sanitisation_Service.filter_special_characters(new_password)
                # Check if new password is the same as the old password
                if new_password == password:
                    print("New password cannot be the same as the old password.\n")
                else:
                    # Ask user for phrase
                    phrase = input("Enter your phrase: ")
                    # Authenticate phrase
                    if login_service.authenticate_phrase(phrase):
                        # Change password
                        login_service.change_password(new_password)
                        print("Password changed successfully.\n")
                        # Create logger to log password change
                        return True
                    else:
                        print("Phrase incorrect.\n")
                        # Create logger to log failed password change
                        return False
            else:
                print("Passwords do not match.\n")
                # Create logger to log failed password change
                return False

    # Will live in here for now
    def change_phrase(self):
        """Changes user phrase"""
        # Ask user for reauthentication
        username, password = self.request_login_details()
        # Create instance of Login_Service class
        login_service = Login_Service(username, password)
        # Authenticate user credentials
        if login_service.authenticate_user_credentials():
            # Ask user for new phrase
            new_phrase = input("New Phrase: ")
            # Ask user to confirm new phrase
            new_phrase_confirmation = input("Confirm New Phrase: ")
            # Check if new phrase matches confirmation
            if new_phrase == new_phrase_confirmation:
                    new_phrase = Input_Sanitisation_Service.sanitise_phrase(new_phrase)
                    login_service.change_phrase(new_phrase)
                    print("Phrase changed successfully.\n")
                    # Create logger to log phrase change
                    return True
            else:
                print("Phrases do not match.\n")
                # Create logger to log failed phrase change
                return False
        else:
            print("Incorrect credentials.\n")
            # Create logger to log failed login attempt
            return False
        
    def connect_login_service(self, login_service):
        """Connects the login service"""
        self.login_service = login_service

    def connect_action_controller(self, action_controller):
        """Connects the action controller"""
        self.action_controller = action_controller
    
