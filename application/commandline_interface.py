"""
    This file contains the CommandLineInterface class
"""

# Imports
import getpass

# CommandLineInterface class
# This class will be responsible for handling user input
class CommandLineInterface:
    #def __init__(self):
        #self.login_service = None # Initialise login_service attribute
        #self.selection = selection
        #self.confirmation = confirmation
        #self.user = User()  # Will be an instance of the User class

    def greeting(self, username): # TESTED AND WORKING
        """Display greeting message"""
        print(f"""
        -------------------------
        Welcome, {username}!
        -------------------------\n""")

    def get_user_information(self, attribute=None): # TODO: TEST AND DEBUG
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

    def request_login_details(self): # TESTED AND WORKING
        """Request user login details"""
        username = input("Username: ")
        password = getpass.getpass("Password: ", stream=None)
        return username, password
    
    def request_password(self):
        """Requests user to re-enter password"""
        password = getpass.getpass("Password: ", stream=None)
        return password

    def ask_for_selection(self): # TESTED AND WORKING
        """Request user selection"""
        selection = input("Enter your selection: ")
        print("\n")
        return selection

    def ask_for_confirmation(self): # TESTED AND WORKING
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

    def display_user_menu(self, username): # TESTED AND WORKING
        """Display user menu options"""
        self.greeting(username) # Display greeting message
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

    def display_main_menu(self): # TESTED AND WORKING
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
                    #self.display_user_menu(username)
                    self.display_test_menu(username)
                else:
                    # Create logger to log failed login attempt
                    pass
            elif selection == '2':
                # Handle Exit
                print("Exiting...\n")
                return True # Confirms exit
            else:
                print("Invalid selection.\n")

    # Will live in here for now
    def change_password(self): # TESTED AND WORKING
        """Changes user password"""
        # Ask user for reauthentication
        password = self.request_password()
        # Authenticate user credentials
        if self.login_service.check_password(password):
            self.login_service.display_password_requirements()
            while True:
                # Ask user for new password
                new_password = getpass.getpass("New Password: ", stream=None)
                # Check that new password is within constraints
                if not self.sanitisation_service.validate_password(new_password):
                    continue
                # Ask user to confirm new password
                new_password_confirmation = getpass.getpass("Confirm New Password: ", stream=None)
                # Check if new password matches confirmation
                if new_password == new_password_confirmation:
                    # Sanitise password
                    new_password = self.sanitisation_service.filter_special_characters(new_password)
                    # Check if new password is the same as the old password
                    if new_password == password:
                        print("New password cannot be the same as the old password.\n")
                    else:
                        # Ask user for phrase
                        phrase = input("Enter your phrase: ")
                        # Authenticate phrase
                        if self.login_service.authenticate_phrase(phrase):
                            # Change password
                            self.login_service.change_password(new_password)
                            self.login_service.set_password(new_password)
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
        else:
            print("Password incorrect.\n")
            # Create logger to log failed password change
            return False

    # Will live in here for now
    def change_phrase(self): # TESTED AND WORKING
        """Changes user phrase"""
        # Ask user for reauthentication
        password = self.request_password()
        # Authenticate user credentials
        if self.login_service.check_password(password):
            while True:
                # Ask user for new phrase
                new_phrase = input("New Phrase: ")
                # Check new phrase against stored phrase
                if not self.login_service.check_phrase(new_phrase):
                    print("New phrase cannot be the same as the old phrase.\n")
                    continue
                # Ask user to confirm new phrase
                new_phrase_confirmation = input("Confirm New Phrase: ")
                # Check if new phrase matches confirmation
                if new_phrase == new_phrase_confirmation:
                        sanitised_phrase = self.sanitisation_service.sanitise_phrase(new_phrase)
                        self.login_service.change_phrase(sanitised_phrase)
                        print("Phrase changed successfully.\n")
                        # Create logger to log phrase change
                        return True
                else:
                    print("Phrases do not match.\n")
                    # Create logger to log failed phrase change
                    return False
        else:
            print("Incorrect password.\n")
            # Create logger to log failed login attempt
            return False
        
    def connect_login_service(self, login_service): # TESTED AND WORKING
        """Connects the login service"""
        self.login_service = login_service

    def connect_action_controller(self, action_controller): # TESTED AND WORKING
        """Connects the action controller"""
        self.action_controller = action_controller
    
    def connect_sanitisation_service(self, sanitisation_service): # TESTED AND WORKING
        """Connects the sanitisation service"""
        self.sanitisation_service = sanitisation_service
    
    def connect_encryption_service(self, encryption_service):
        """Connects the encryption service"""
        self.encryption_service = encryption_service
    
    def display_test_menu(self, username): # FOR TESTING ONLY: TODO REMOVE THIS
        print("Test Menu")
        self.greeting(username)
        while True:
            print("\n1. Change Password")
            print("\n2. Change Phrase")
            print("\n3. Ask for confirmation")
            print("\n4. Retrieve user attributes")
            print("\n99. Exit\n")

            # Request user selection
            selection = self.ask_for_selection()

            # Handle user selection
            if selection == '1':
                self.change_password()
            elif selection == '2':
                self.change_phrase()
            elif selection == '3':
                self.ask_for_confirmation()
            elif selection == '4':
                attribute = input("Attribute: ")
                if attribute is not None:
                    print(self.get_user_information(attribute))
                elif attribute == "":
                    print(self.get_user_information())
            elif selection == '99':
                # Handle Exit
                print("Exiting...\n")
                break
