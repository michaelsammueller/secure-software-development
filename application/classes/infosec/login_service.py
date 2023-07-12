"""
    This file contains the Login_Service class
"""

# Imports
import bcrypt
import datetime

# Login Class
class Login_Service:
    def __init__(self):
        self.__username = ''
        self.__password = ''
    
    def set_username(self, username):
        """Sets username"""
        self.__username = username

    def set_password(self, password):
        self.__password = password
    
    def get_loggedin_username(self):
        """Returns username of logged in user"""
        return self.__username

    def check_phrase_required(self):
        """Check last login"""
        try:
            last_login = self.__db_manager.do_select(
                'SELECT last_login_at FROM users WHERE username = ?', (self.__username,))
            last_login = last_login[0][0]

            # If last_login is None, return True
            if last_login is None:
                return False
            else:
                last_login = datetime.datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S')
                today = datetime.date.today()

                # Calculate difference in months
                months_diff = (today.year - last_login.year) * 12 + (today.month - last_login.month)

                # Check if difference is greater than 3 months
                if months_diff > 3:
                    return True
                else:
                    return False
        except Exception as e:
            print(f"An error occured: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
            return True
    
    def check_phrase(self, new_phrase):
        """Checks new phrase against stored phrase"""
        try:
            stored_phrase = self.__db_manager.do_select('SELECT phrase FROM users WHERE username = ?', (self.__username,))
            stored_phrase = stored_phrase[0][0] # Get stored phrase from tuple

            # Check if new phrase matches stored phrase
            if new_phrase == stored_phrase:
                return False
            else:
                return True
        except Exception as e:
            print(f"An error occured: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
            return True

    def authenticate_user_credentials(self):
        """Authenticate user credentials"""
        try:
            result = self.__db_manager.do_select(
                'SELECT password FROM users WHERE username = ?', (self.__username,))
            if result:
                stored_password = result[0][0]
                # Compare entered password with stored password
                if bcrypt.checkpw(self.__password.encode('utf-8'), stored_password):
                    return True
                else:
                    print("Invalid username or password.\n")
                    return False
            else:
                print("No such user.\n")
        except Exception as e:
            print(f"An error occured: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
            return False

    def authenticate_phrase(self, phrase):
        """Authenticate phrase"""
        try:
            secret_phrase = self.__db_manager.do_select(
                'SELECT phrase FROM users WHERE username = ?', (self.__username,))
            secret_phrase = secret_phrase[0][0] # Get secret phrase from tuple
            if phrase == secret_phrase:
                return True
            else:
                print("Invalid phrase.\n")
                return False
        except Exception as e:
            print(f"Unable to authenticate phrase: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
            return False

    def login(self, username, password):
        """Calls upon the other methods to login the user"""
        # Set username and password
        self.set_username(username)
        self.set_password(password)
        # Authenticate user credentials
        if self.authenticate_user_credentials():
            if self.check_phrase_required():
                phrase = input("Enter your secret phrase: ")
                sanitised_phrase = self.__input_sanitisation_service.sanitise_phrase(phrase)
                if self.authenticate_phrase(sanitised_phrase):
                    print("\nLogin successful.\n")
                    return True
                else:
                    print("\nLogin failed.\n")
                    return False
            else:
                print("\nLogin successful.\n")
                return True
        else:
            print("\nLogin failed.\n")
            return False

    # Changes password in database
    def change_password(self, new_password):
        """Change user password"""
        try:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())  # Hash password
            self.__db_manager.do_update('UPDATE users SET password = ? WHERE username = ?',
                            (hashed_password, self.__username), dry=False)
            print("Password changed successfully.\n")
            return True
        except Exception as e:
            print(f"Unable to change password: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
            return False
    
    # Changes secret phrase in database
    def change_phrase(self, new_phrase):
        """Change secret phrase"""
        try:
            self.__db_manager.do_update('UPDATE users SET phrase = ? WHERE username = ?',
                             (new_phrase, self.__username), dry=False)
            print("Secret phrase changed successfully.\n")
            return True
        except Exception as e:
            print(f"Unable to change secret phrase: {e}\n")
            # Create logger to log error
            json = {
                'activity_type': 'event',
                'severity': 'warning',
                'event': {
                    'type': 'error',
                    'details': {
                        'message': f"An error occured: {e}"
                    }
                }
            }
            self.__logger.log(json)
            return False
    
    def display_password_requirements(self):
        print("Password Requirements\n")
        print("1. Must be between 8 and 64 characters long\n")
    
    def connect_encryption_service(self, encryption_service):
        """Connects the encryption service"""
        self.__encryption_service = encryption_service
    
    def connect_input_sanitisation_service(self, input_sanitisation_service):
        """Connects the input sanitisation service"""
        self.__input_sanitisation_service = input_sanitisation_service
    
    def connect_logger(self, logger):
        """Connects the logger"""
        self.__logger = logger
    
    def connect_db_manager(self, db_manager):
        """Connects the db manager"""
        self.__db_manager = db_manager
