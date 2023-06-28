"""
    This file contains the Login_Service class
"""

# Imports
from imports import bcrypt, DBManager, datetime, Input_Sanitisation


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
                'SELECT last_login FROM users WHERE username = ?', (self.username,))
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
                'SELECT password, salt FROM users WHERE username = ?', (self.username,))
            if result:
                stored_password = result[0]
                salt = result[1]
                # Hash the entered password with the stored salt
                hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt.encode('utf-8'))
                # Compare the hashed password with the stored password
                if stored_password == hashed_password:
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
                sanitiser = Input_Sanitisation()
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
