"""
    This file contains the Login_Service class
"""

# Imports
import bcrypt
import datetime
import time
import getpass
from classes.dbmanager import DBManager

# Login Class
class Login_Service:
    def __init__(self):
        self.__username = ''
        self.__password = ''
        self.__login_attempts = 0
        self.__lock_time = None
        self.__stop_timer = False
    
    def set_username(self, username):
        """Sets username"""
        self.__username = username

    def set_password(self, password):
        encrypted_password = self.__encryption_service.encrypt(password)
        self.__password = encrypted_password
    
    def set_login_attempts(self, login_attempts):
        """Sets number of login attempts"""
        self.__login_attempts = login_attempts
    
    def get_password(self):
        """Decrypts password and returns it"""
        decrypted_password = self.__encryption_service.decrypt(self.__password)
        return decrypted_password
    
    def get_stop_timer(self):
        """Returns stop timer"""
        return self.__stop_timer
    
    def get_login_attempts(self):
        """Returns number of login attempts"""
        return self.__login_attempts
    
    def get_lock_time(self):
        """Returns lock time"""
        return self.__lock_time
    
    def check_password(self, password):
        """Reauthenticates user by checking password"""
        auth_password = self.get_password()
        # Check that password is correct
        if password == auth_password:
            return True
        else:
            return False
    
    def get_loggedin_username(self):
        """Returns username of logged in user"""
        return self.__username

    def get_loggedin_user_id(self):
        """Returns user id of logged in user"""
        user_id = self.__db_manager.do_select('SELECT id FROM users WHERE username = ?', (self.__username,))
        user_id = user_id[0][0]
        return user_id
    
    def get_loggedin_user_uuid(self):
        """Returns uuid of logged in user"""
        uuid = self.__db_manager.do_select('SELECT uuid FROM users WHERE username = ?', (self.__username,))
        uuid = uuid[0][0]
        return uuid

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
                # Get current password
                password = self.get_password()
                # Compare entered password with stored password
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    return True
                else:
                    print("Invalid username or password.\n")
                    self.__login_attempts += 1
                    return False
            else:
                self.__login_attempts += 1
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
    
    def increment_attempts(self):
        """Increments login attempts"""
        self.__login_attempts += 1

    def lockdown_required(self):
        """Checks if number of failed attempts has reached the limit"""
        if self.__login_attempts >= 5:
            return True
        else:
            return False
    
    def lockdown(self):
        """Locks the application"""
        current_time = time.time()
        self.__lock_time = current_time
    
    def check_lockdown(self):
        """Checks if the application is locked and returns the remaining time"""
        current_time = time.time()
        if self.__lock_time is None:
            return False
        if current_time - self.__lock_time >= 10:
            self.__lock_time = None
            return False
        else:
            remaining_time = int(10 - (current_time - self.__lock_time))
            return remaining_time
    
    def start_lockdown_timer(self):
        """Starts the lockdown timer"""
        self.__lock_time = time.time()

    def stop_lockdown_timer(self):
        """Stops the lockdown timer"""
        self.__lock_time = None

    def password_input_thread(self):
        """Thread function to ask for superadmin access"""
        while True:
            if not self.check_lockdown():
                self.set_login_attempts(0)
                print("\n1. Login")
                print("2. Exit\n")
                break
            else:
                username = input("Enter admin username: ")
                password = getpass.getpass("Enter admin password: ")
                # Create a thread safe connection to the database

                query = 'SELECT password, role_id FROM users WHERE username = ?'
                user = self.__db_manager.do_select(query, (username,))
                if user:
                    stored_password = user[0]['password']
                    role_id = user[0]['role_id']
                    if role_id == 1 and bcrypt.checkpw(password.encode(), stored_password):
                        self.__stop_timer = True
                        break
                    else:
                        print("This user is not an admin.\n")
                else:
                    print("This user does not exist.\n")
    
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

