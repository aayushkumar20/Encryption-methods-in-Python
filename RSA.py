# Write a python program to implement RSA algorithm
# functionality 
# ask for a message from the user
# generate public and private keys
# encrypt the message using public key
# decrypt the cipher text using private key
# generate_keys() - generates public and private keys
# encrypt_message() - encrypts a message using public key
# decrypt_message() - decrypts the cipher text using private key
# input parameters - message, public key for encrypt_message() function
# input parameters - cipher text, private key for decrypt_message() function
# output consist of 
# 1. RSA public key
# 2. RSA private key
# 3. Encrypted message
# 4. Decrypted message
# 5. original message

import rsa
import random
import math

class RSA:
    # constructor
    def __init__(self):
        # message to be encrypted
        self.message = "Aayush Kumar (20BCY10045))"
        # p and q are two random prime numbers
        self.p = 0
        self.q = 0
        # n = p * q
        self.n = 0
        # phi = (p - 1) * (q - 1)
        self.phi = 0
        # e is the public key exponent
        self.e = 0
        # d is the private key exponent
        self.d = 0
        # public key
        self.public_key = []
        # private key
        self.private_key = []
        # encrypted message
        self.encrypted_message = []
        # decrypted message
        self.decrypted_message = []
    # generate public and private keys
    def generate_keys(self):
        # generate two random prime numbers
        self.p = self.generate_prime()
        self.q = self.generate_prime()
        # calculate n
        self.n = self.p * self.q
        # calculate phi
        self.phi = (self.p - 1) * (self.q - 1)
        # generate e
        self.e = self.generate_e()
        # generate d
        self.d = self.generate_d()
        # public key
        self.public_key = [self.e, self.n]
        # private key
        self.private_key = [self.d, self.n]
    # generate prime numbers
    def generate_prime(self):
        while True:
            # generate a random number
            num = random.randint(100, 1000)
            # check if the number is prime
            if self.is_prime(num):
                return num
    # check if a number is prime
    def is_prime(self, num):
        # check if the number is even
        if num % 2 == 0:
            return False
        # check if the number is divisible by any odd number
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    # generate e
    def generate_e(self):
        # generate a random number
        while True:
            e = random.randint(2, self.phi)
            # check if e and phi are co-prime
            if self.is_coprime(e, self.phi):
                return e
    # check if two numbers are co-prime
    def is_coprime(self, num1, num2):
        return math.gcd(num1, num2) == 1
    # generate d
    def generate_d(self):
        # generate d
        d = self.mod_inverse(self.e, self.phi)
        return d
    # calculate the modular multiplicative inverse
    def mod_inverse(self, a, m):
        # find modular multiplicative inverse
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
    # encrypt the message
    def encrypt_message(self):
        # convert the message to numbers
        message_num = self.convert_to_numbers(self.message)
        # encrypt the message
        for num in message_num:
            self.encrypted_message.append(self.encrypt(num, self.public_key))
    # convert the message to numbers
    def convert_to_numbers(self, message):
        message_num = []
        for char in message:
            message_num.append(ord(char))
        return message_num
    # encrypt the message
    def encrypt(self, num, public_key):
        return (num ** public_key[0]) % public_key[1]
    # decrypt the message
    def decrypt_message(self):
        # decrypt the message
        for num in self.encrypted_message:
            self.decrypted_message.append(self.decrypt(num, self.private_key))
    # decrypt the message
    def decrypt(self, num, private_key):
        return (num ** private_key[0]) % private_key[1]
    # convert the numbers to message
    def convert_to_message(self, message_num):
        message = ""
        for num in message_num:
            message += chr(num)
        return message
    # print the keys
    def print_keys(self):
        print("RSA public key: ", self.public_key)
        print("RSA private key: ", self.private_key)
    # print the encrypted message
    def print_encrypted_message(self):
        print("Encrypted message: ", self.encrypted_message)
    # print the decrypted message
    def print_decrypted_message(self):
        print("Decrypted message: ", self.decrypted_message)
    # print the original message
    def print_original_message(self):
        print("Original message: ", self.message)
    
    # main function
    def main(self):
        print("Made by: Aayush Kumar")
        print("20BCY10045")
        print("Github: https://github.com/aayushkumar20/Encryption-methods-in-Python")
        print("Message: ", self.message)
        # generate public and private keys
        self.generate_keys()
        # print the keys
        self.print_keys()
        # encrypt the message
        self.encrypt_message()
        # print the encrypted message
        self.print_encrypted_message()
        # decrypt the message
        self.decrypt_message()
        # print the decrypted message
        self.print_decrypted_message()
        # convert the numbers to message
        self.decrypted_message = self.convert_to_message(self.decrypted_message)
        # print the original message
        self.print_original_message()

if __name__ == "__main__":
    rsa = RSA()
    rsa.main()
