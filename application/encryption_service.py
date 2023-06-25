# Imports
from imports import Fernet


# Encryption Service Class
class Encryption_Service:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt(self, data):
        """Encrypt data"""
        cipher_suite = Fernet(self.secret_key)
        encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
        return encrypted_data

    def decrypt(self, encrypted_data):
        """Decrypt data"""
        cipher_suite = Fernet(self.secret_key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')


# Test
# secret_key = Fernet.generate_key()
# encryption_service = Encryption_Service(secret_key)
# data = "Hello World!"
# encrypted_data = encryption_service.encrypt(data)
# print(encrypted_data)
# decrypted_data = encryption_service.decrypt(encrypted_data)
# print(decrypted_data)
