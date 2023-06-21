# Imports
from imports import bcrypt

# Encryption Service Class
class Encryption_Service:

    def __init__(self, secret, data):
        self.secret = secret
        self.data = data
    
    def encrypt(self, secret, data):
        """Encrypt data"""
        encrypted_data = secret.encrypt(data.encode())
        return encrypted_data
    
    def decrypt(self, secret, data):
        """Decrypt data"""
        decrypted_data = secret.decrypt(data).decode()
        return decrypted_data
