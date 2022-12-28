import random
import math
import hashlib
from Crypto.Cipher import AES
from secrets import token_bytes

def modInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def generate_key(p, q):
    if (not isPrime(p) or not isPrime(q)):
        raise ValueError('Both numbers must be prime.')
    elif (p == q):
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)
    d = modInverse(e, phi)
    return ((p, q, d), (n, e))

def encrypt_message(public_key: tuple[int,int],msg: str):
    n,e = public_key
    encrypted =" "
    for letter in msg:
        encrypted = encrypted + chr((ord(letter) ** e) % n)
    return encrypted

def decrypt_message(private_key: tuple[int,int,int],ciphertext: str):
    p,q,d=private_key
    n=p*q
    decrypted =" "
    for letter in ciphertext:
        decrypted = decrypted + chr((ord(letter) ** d) % n)
    return decrypted

key= token_bytes(16)

def encrypt(msg):

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag= cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext=cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

msg=(input('enter a message: '))
hasher=hashlib.sha512(msg.encode())
print('hashcode: '+hasher.hexdigest())
r1,r2=generate_key(7,11)
m1=encrypt_message(r2,hasher.hexdigest())
msg1=msg+m1
print('new message: '+msg1)

nonce, ciphertext, tag = encrypt(msg1)
plaintext = decrypt(nonce, ciphertext, tag)
print(f'cipher text: {ciphertext}')
if not plaintext:
    print('message is corrupted')
else:
    print(f'plain text: {plaintext}')

msg2,msg3=plaintext.split(' ')
print('Message entered:'+msg2)
print('encrypted hashcode of the message:'+msg3)

f=decrypt_message(r1,msg3)
print(f'decrypted hashcode of the message: {f}')
