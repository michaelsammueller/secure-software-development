"""
    This file contains the CommandLineInterface class
"""

# Imports
import getpass
import threading


# CommandLineInterface class
# This class will be responsible for handling user input
class CommandLineInterface:
    def __init__(self):
        self.__timer_thread = None

    def greeting(self, username):
        """Display greeting message"""
        print(f"""
        -------------------------
        Welcome, {username}!
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

    def request_password(self):
        """Requests user to re-enter password"""
        password = getpass.getpass("Old password: ", stream=None)
        return password

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

    def display_user_menu(self, username):
        """Display user menu options"""
        self.greeting(username)  # Display greeting message
        while True:
            options = self.__action_controller.get_actions()
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
                params = self.__action_controller.get_action_params(options[selection - 1])
                details = {}
                print("\nRequesting details...")
                while True:
                    for param in params:
                        while True:
                            if not param[1]:  # only field name provided
                                print(f"{param[0]}")
                            else:  # field name and options provided
                                print(f"Options for {param[0]}: {param[1]}")
                            response = self.ask_for_selection()
                            if param[2]:
                                # validate input
                                if not self.__sanitisation_service.validate(response,
                                                                            param[2], param[1]):
                                    continue
                            details[param[0]] = response
                            break
                    # Confirm details
                    if details:
                        print("\nAre you happy to submit the following details?")
                        print(f"{[f'{key}: {value}' for key, value in details.items()]}")
                        if self.ask_for_confirmation():
                            break
                        else:
                            continue
                    else:
                        break

                # Perform action
                results = self.__action_controller(options[selection - 1], details)
                if results:
                    print("\nResults...")
                    try:
                        # dict results
                        print(f"{[f'{key}: {value}' for key, value in results.items()]}")
                    except:
                        for result in results:
                            print(f"{[f'{key}: {value}' for key, value in result.items()]}")
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
        # Adding color options for user interface
        COLOR_GREEN = '\033[38;2;0;128;0m'
        COLOR_RESET = '\033[0m'
        while True:
            print(COLOR_GREEN + """
     █████  ██   ██ ███    ███
    ██   ██ ██   ██ ████  ████
    ███████ ███████ ██ ████ ██
    ██   ██ ██   ██ ██  ██  ██
    ██   ██ ██   ██ ██      ██
                """ + COLOR_RESET)
            print("""
----------------------------------
Astronaut Health Monitoring System
----------------------------------
    (C) 2023, SecureSpace\n
""")
            print("\n1. Login")
            print("2. Exit\n")

            # Check if application is locked
            remaining_time = self.__login_service.check_lockdown()
            if remaining_time > 0:
                if self.__timer_thread is None:
                    minutes = remaining_time // 60
                    seconds = remaining_time % 60
                    print(f"""
                          Application is locked.
                          Please try again in {minutes} minutes and {seconds} seconds.
                          \n""")

                    self.__timer_thread = threading.Thread(
                        target=self.__login_service.password_input_thread,)
                    self.__timer_thread.start()

                self.__timer_thread.join()

                stop_timer = self.__login_service.get_stop_timer()
                if stop_timer:  # Stop the timer
                    self.__login_service.stop_lockdown_timer()
                    self.__login_service.set_login_attempts(0)
            # Request user selection
            selection = self.ask_for_selection()

            # Check if lockdown is required
            if self.__login_service.lockdown_required():
                print("Exceeded maximum amount of login attempts. Please try again later.\n")
                # Lock application
                self.__login_service.lockdown()
                # Log the lockdown event
                json = {
                    'user': 'system',
                    'activity_type': 'event',
                    'severity': 'danger',
                    'event': {
                        'type': 'lockdown',
                        'details': {
                            'message': 'Exceeded maximum amount of login attempts'
                        }
                    }
                }
                self.__logger.log(json)
                continue

            # Handle user selection
            if selection == '1':
                username, password = self.request_login_details()  # Request user login details
                # Handle Login
                if self.__login_service.login(username, password):
                    # self.display_test_menu(username)
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'info',
                        'event': {
                            'type': 'successful login',
                            'details': {
                                'username': username,
                                'password': password
                            }
                        }
                    }
                    self.__logger.log(json)
                    self.display_user_menu(username)
                else:
                    self.__login_service.increment_attempts()
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'warning',
                        'event': {
                            'type': 'failed login',
                            'details': {
                                'username': username,
                                'password': password
                            }
                        }
                    }
                    self.__logger.log(json)
            elif selection == '2':
                # Handle Exit
                print("Exiting...\n")
                # Logging event
                json = {
                    'user': 'Application',
                    'activity_type': 'event',
                    'severity': 'info',
                    'event': {
                        'type': 'exit',
                        'details': {
                            'event': 'Application was closed from main menu',
                            'shutdown': 'Planned'
                        }
                    }
                }
                self.__logger.log(json)
                return True  # Confirms exit
            else:
                print("Invalid selection.\n")

    # Will live in here for now
    def change_password(self):
        """Changes user password"""
        # Ask user for reauthentication
        password = self.request_password()
        # Authenticate user credentials
        if self.__login_service.check_password(password):
            # Log successful reauthentication
            username = self.__login_service.get_loggedin_username()
            password = self.__login_service.get_password()
            # Create json file
            json = {
                'user': username,
                'activity_type': 'event',
                'severity': 'info',
                'event': {
                    'type': 'successful reauthentication',
                    'details': {
                        'username': username,
                        'password': password
                    }
                }
            }
            # Log event
            self.__logger.log(json)
            # Display password requirements
            self.__login_service.display_password_requirements()
            while True:
                # Ask user for new password
                new_password = getpass.getpass("New Password: ", stream=None)
                # Check that new password is within constraints
                if not self.__sanitisation_service.validate_password(new_password):
                    # Log failed password change
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'info',
                        'event': {
                            'type': 'failed password change',
                            'details': {
                                'username': username,
                                'new password': new_password,
                                'reason': 'Password did not meet requirements'
                            }
                        }
                    }
                    self.__logger.log(json)
                    # Display password requirements again and ask user for new password
                    continue
                # Ask user to confirm new password
                new_password_confirmation = getpass.getpass("Confirm New Password: ", stream=None)
                # Check if new password matches confirmation
                if new_password == new_password_confirmation:
                    # Check if new password is the same as the old password
                    if new_password == password:
                        print("New password cannot be the same as the old password.\n")
                        # Log failed password change
                        json = {
                            'user': username,
                            'activity_type': 'event',
                            'severity': 'info',
                            'event': {
                                'type': 'failed password change',
                                'details': {
                                    'username': username,
                                    'new password': new_password,
                                    'reason': 'New password cannot be the same as the old password'
                                }
                            }
                        }
                        self.__logger.log(json)
                    else:
                        # Ask user for phrase
                        phrase = input("Enter your phrase: ")
                        # Authenticate phrase
                        if self.__login_service.authenticate_phrase(phrase):
                            # Change password
                            self.__login_service.change_password(new_password)
                            self.__login_service.set_password(new_password)
                            # Create logger to log password change
                            json = {
                                'user': username,
                                'activity_type': 'event',
                                'severity': 'info',
                                'event': {
                                    'type': 'successful password change',
                                    'details': {
                                        'username': username,
                                        'old password': password,
                                        'new password': new_password
                                    }
                                }
                            }
                            self.__logger.log(json)
                            return True
                        else:
                            print("Phrase incorrect.\n")
                            # Create logger to log failed password change
                            json = {
                                'user': username,
                                'activity_type': 'event',
                                'severity': 'warning',
                                'event': {
                                    'type': 'failed password change',
                                    'details': {
                                        'username': username,
                                        'old password': password,
                                        'new password': new_password,
                                        'phrase': phrase,
                                        'reason': 'Phrase did not match stored phrase.'
                                    }
                                }
                            }
                            self.__logger.log(json)
                            return False
                else:
                    print("Passwords do not match.\n")
                    # Create logger to log failed password change
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'info',
                        'event': {
                            'type': 'failed password change',
                            'details': {
                                'username': username,
                                'new password': new_password,
                                'new password confirmation': new_password_confirmation,
                                'reason': 'New password did not match confirmation'
                            }
                        }
                    }
                    self.__logger.log(json)
                    return False
        else:
            print("Password incorrect.\n")
            # Create logger to log failed password change
            json = {
                'user': self.__login_service.get_loggedin_username(),
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'failed password change',
                    'details': {
                        'username': self.__login_service.get_loggedin_username(),
                        'password': password,
                        'reason': 'Password did not match stored password'
                    }
                }
            }
            self.__logger.log(json)
            return False

    # Will live in here for now
    def change_phrase(self):
        """Changes user phrase"""
        # Ask user for reauthentication
        password = self.request_password()
        # Authenticate user credentials
        if self.__login_service.check_password(password):
            # Log successful reauthentication
            username = self.__login_service.get_loggedin_username()
            password = self.__login_service.get_password()
            # Create json file
            json = {
                'user': username,
                'activity_type': 'event',
                'severity': 'info',
                'event': {
                    'type': 'successful reauthentication',
                    'details': {
                        'username': username,
                        'password': password
                    }
                }
            }
            # Log event
            self.__logger.log(json)
            while True:
                # Ask user for new phrase
                new_phrase = input("New Phrase: ")
                # Check new phrase against stored phrase
                if not self.__login_service.check_phrase(new_phrase):
                    print("New phrase cannot be the same as the old phrase.\n")
                    # Log failed phrase change
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'info',
                        'event': {
                            'type': 'failed phrase change',
                            'details': {
                                'username': username,
                                'new phrase': new_phrase,
                                'reason': 'New phrase cannot be the same as the old phrase'
                            }
                        }
                    }
                    self.__logger.log(json)
                    continue
                # Ask user to confirm new phrase
                new_phrase_confirmation = input("Confirm New Phrase: ")
                # Check if new phrase matches confirmation
                if new_phrase == new_phrase_confirmation:
                    sanitised_phrase = self.__sanitisation_service.sanitise_phrase(new_phrase)
                    self.__login_service.change_phrase(sanitised_phrase)
                    print("Phrase changed successfully.\n")
                    # Create logger to log phrase change
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'info',
                        'event': {
                            'type': 'successful phrase change',
                            'details': {
                                'username': username,
                                'old phrase': self.__login_service.get_phrase(),
                                'new phrase': sanitised_phrase
                            }
                        }
                    }
                    self.__logger.log(json)
                    return True
                else:
                    print("Phrases do not match.\n")
                    # Create logger to log failed phrase change
                    json = {
                        'user': username,
                        'activity_type': 'event',
                        'severity': 'info',
                        'event': {
                            'type': 'failed phrase change',
                            'details': {
                                'username': username,
                                'new phrase': new_phrase,
                                'new phrase confirmation': new_phrase_confirmation,
                                'reason': 'New phrase did not match confirmation'
                            }
                        }
                    }
                    self.__logger.log(json)
                    return False
        else:
            print("Incorrect password.\n")
            # Create logger to log failed login attempt
            json = {
                'user': username,
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'failed password change',
                    'details': {
                        'username': username,
                        'password': password,
                        'reason': 'Password did not match stored password'
                    }
                }
            }
            self.__logger.log(json)
            return False

    def connect_login_service(self, login_service):
        """Connects the login service"""
        self.__login_service = login_service

    def connect_action_controller(self, action_controller):
        """Connects the action controller"""
        self.__action_controller = action_controller

    def connect_sanitisation_service(self, sanitisation_service):
        """Connects the sanitisation service"""
        self.__sanitisation_service = sanitisation_service

    def connect_encryption_service(self, encryption_service):
        """Connects the encryption service"""
        self.__encryption_service = encryption_service

    def connect_logger(self, logger):
        """Connects the logger"""
        self.__logger = logger

    def connect_download_service(self, download_service):
        """Connects the download service"""
        self.__download_service = download_service

    def connect_db_manager(self, db_manager):
        """Connects the database manager"""
        self.__db_manager = db_manager
