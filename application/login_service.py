# Imports
from imports import sqlite3, bcrypt


# Login Class
class Login_Service:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate_user_credentials(self, username, password):
        """Authenticate user credentials"""
        connect = sqlite3.connect('data/securespace.db')
        cursor = connect.cursor()

        # Check if the username exists in the database and retrieve the stored password and salt
        cursor.execute('SELECT password, salt FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        if result:
            stored_password = result[0]
            salt = result[1]
            # Hash the entered password with the stored salt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
            # Compare the hashed password with the stored password
            if stored_password == hashed_password:
                print('Login successful!\n')
                return True
        print("Invalid username or password.\n")
        connect.close()
        return False
