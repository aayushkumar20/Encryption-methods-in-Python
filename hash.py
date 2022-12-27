import hashlib

print("Aayush Kumar (20BCY10045)")
print("")
name = "20BCY10045 Aayush Kumar"
print("Name is : " + name)
hash = hashlib.sha512(name.encode())
print("The hexadecimal equivalent of name is : ")
n = print(hash.hexdigest())
