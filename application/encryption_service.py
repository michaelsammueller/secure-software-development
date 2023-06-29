"""
    This file contains the Encryption_Service class
"""

# Imports
from imports import Fernet


# Encryption Service Class
class Encryption_Service:
    def __init__(self):
        self._secret_key = b'RSzJyYagLgs1ZasBK5zBjoe54qSQzZtLmnfiy3L3aUA='

    def encrypt(self, data):
        """Encrypt data"""
        cipher_suite = Fernet(self._secret_key)
        encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
        # Create logger to log successful encryption
        return encrypted_data

    def decrypt(self, encrypted_data):
        """Decrypt data"""
        cipher_suite = Fernet(self._secret_key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        # Create logger to log successful decryption
        return decrypted_data.decode('utf-8')


# Test
# secret_key = Fernet.generate_key()
# encryption_service = Encryption_Service(secret_key)
# data = "Hello World!"
# encrypted_data = encryption_service.encrypt(data)
# print(encrypted_data)
# decrypted_data = encryption_service.decrypt(encrypted_data)
# print(decrypted_data)
