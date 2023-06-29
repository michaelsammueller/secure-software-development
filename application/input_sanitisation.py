"""
    This file contains the Login_Service class
"""

# Imports
from imports import bcrypt, datetime
from classes.dbmanager import DBManager
from input_sanitisation import Input_Sanitisation_Service

# Login Class
class Login_Service:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_phrase_required(self):
        """Check last login"""
        try:
            dbman = DBManager()  # Create DBManager instance
            last_login = dbman.do_select(
                'SELECT last_login_at FROM users WHERE username = ?', (self.username,))
            last_login = last_login[0][0]

            # If last_login is None, return True
            if last_login is None:
                return False
            else:
                last_login = datetime.datetime.fromtimestamp(last_login)
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
            return True

    def authenticate_user_credentials(self):
        """Authenticate user credentials"""
        try:
            dbman = DBManager()  # Create DBManager instance
            result = dbman.do_select(
                'SELECT password FROM users WHERE username = ?', (self.username,))
            if result:
                stored_password = result[0][0]
                # Compare entered password with stored password
                if bcrypt.checkpw(self.password.encode('utf-8'), stored_password):
                    return True
                else:
                    print("Invalid username or password.\n")
                    # Create logger to log failed login
                    return False
        except Exception as e:
            print(f"An error occured: {e}\n")
            # Create logger to log error
            return False

    def authenticate_phrase(self, phrase):
        """Authenticate phrase"""
        try:
            dbman = DBManager()  # Create DBManager instance
            secret_phrase = dbman.do_select(
                'SELECT phrase FROM users WHERE username = ?', (self.username,))
            if phrase == secret_phrase:
                return True
            else:
                print("Invalid phrase.\n")
                # Create logger to log failed login
                return False
        except Exception as e:
            print(f"Unable to authenticate phrase: {e}\n")
            # Create logger to log error
            return False

    def login(self):
        """Calls upon the other methods to login the user"""
        if self.authenticate_user_credentials():
            if self.check_phrase_required():
                phrase = input("Enter your secret phrase: ")
                sanitiser = Input_Sanitisation_Service()
                sanitised_phrase = sanitiser.sanitise_phrase(phrase)
                if self.authenticate_phrase(sanitised_phrase):
                    print("Login successful.\n")
                    # Create logger to log successful login
                    return True
                else:
                    print("Login failed.\n")
                    # Create logger to log failed login
                    return False
            else:
                print("Login successful.\n")
                # Create logger to log successful login
                return True
        else:
            print("Login failed.\n")
            # Create logger to log failed login
            return False

    def change_password(self, new_password):
        """Change user password"""
        try:
            dbman = DBManager()  # Create DBManager instance
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())  # Hash password
            dbman.do_update('UPDATE users SET password = ? WHERE username = ?',
                            (hashed_password, self.username))
            print("Password changed successfully.\n")
            # Create logger to log successful password change
            return True
        except Exception as e:
            print(f"Unable to change password: {e}\n")
            # Create logger to log error
            return False
    
    # CHECK DATABASE SCHEMA ONCE PHRASE ADDED
    def change_phrase(self, new_phrase):
        """Change secret phrase"""
        try:
            dbman = DBManager()  # Create DBManager instance
            dbman.do_update('UPDATE users SET phrase = ? WHERE username = ?',
                             (new_phrase, self.username))
            print("Secret phrase changed successfully.\n")
            # Create logger to log successful phrase change
            return True
        except Exception as e:
            print(f"Unable to change secret phrase: {e}\n")
            # Create logger to log error
            return False
