# Write a python program to implement AES algorithm
# functionality 
# Take input as "Aayush Kumar"
# Generate a random key
# Encrypt the message using the key
# generate_key() - function to generate a random key
# encrypt_message() - function to encrypt the message
# decrypt_message() - function to decrypt the message
# input: message to be encrypted
# output consists of AES private key
# original message, encrypted message and decrypted message
# without using Crypto module
# Using simple python functions

import random 
import string
import base64

class Encrypt:
    def __init__(self, message):
        self.message = message
        self.key = self.generate_key()
        self.encrypted_message = self.encrypt_message()
        self.decrypted_message = self.decrypt_message()

    def generate_key(self):
        key = ''.join(random.choice(string.ascii_letters) for i in range(16))
        return key

    def encrypt_message(self):
        encrypted_message = ''
        for i in range(len(self.message)):
            key_c = self.key[i % len(self.key)]
            encrypted_message += chr((ord(self.message[i]) + ord(key_c)) % 256)
        return base64.urlsafe_b64encode(encrypted_message.encode()).decode()

    def decrypt_message(self):
        decrypted_message = ''
        encrypted_message = base64.urlsafe_b64decode(self.encrypted_message).decode()
        for i in range(len(self.message)):
            key_c = self.key[i % len(self.key)]
            decrypted_message += chr((256 + ord(encrypted_message[i]) - ord(key_c)) % 256)
        return decrypted_message
    # main function
if __name__ == '__main__':
    # This Project is implemented by Aayush Kumar
    # on date 24th Dec, 2022
    print("This Project is implemented by Aayush Kumar on date 24th Dec, 2022")
    print("20BCY10045")
    # Let the message be "Aayush Kumar"
    message = "Aayush Kumar 20BCY10045"
    # print the original message
    print("Original Message: ", message)
    encrypt = Encrypt(message)
    # print the key
    print("Key: ", encrypt.key)
    # print the encrypted message
    print("Encrypted Message: ", encrypt.encrypted_message)
    # print the decrypted message
    print("Decrypted Message: ", encrypt.decrypted_message)