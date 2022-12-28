import hashlib
import random

def birthday():
  hashes = {}

  n = 0
  while True:
    s = hex(random.getrandbits(128))[2:] 
    t = hex(random.getrandbits(128))[2:] 
    n += 1
    hs = hashlib.sha1(s.encode()).hexdigest()[:10]
    ht = hashlib.sha1(t.encode()).hexdigest()[:10]
    if hs == ht:
      return (s, t, n)
    elif hs in hashes:
      return (s, hashes[hs], n)
    elif ht in hashes:
      return (t, hashes[ht], n)
    else:
      hashes[hs] = s
      hashes[ht] = t
a = birthday()
b = birthday()
print("Aayush Kumar 20BCY10045")
print("")
print(a)
print(b)
