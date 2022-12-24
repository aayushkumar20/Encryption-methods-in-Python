import hashlib
#print("Hashing Algorithms Available: ")
#print(hashlib.algorithms_available)
#print("Hashing Algorithms Guaranteed: ")
#print(hashlib.algorithms_guaranteed)

#Message = "the quick brown fox jumps over the lazy dog"
#print("The original string is : " + Message)
#hash = hashlib.sha1(Message.encode())
#Message1 = "the quick     brown fox jumps over the lazy dog"
#hash1 = hashlib.sha1(Message1.encode())
#print("The hexadecimal equivalent of hash is : ")
#print(hash.hexdigest())
#print("The hexadecimal equivalent of hash1 is : ")
#print(hash1.hexdigest())

name = "Rouf"
print("name is : " + name)
hash = hashlib.sha1(name.encode())
print("The hexadecimal equivalent of hash is : ")
print(hash.hexdigest())
hash2 = hashlib.sha512(name.encode())
print("The hexadecimal equivalent of hash2 is : ")
n = print(hash2.hexdigest())

# write a program to implement SHA128 encryption algorithm

