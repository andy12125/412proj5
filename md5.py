#converts text to MD5 hash
#uses variable 'text'

import hashlib

text = input ("Enter text to convert to MD5 Hash: ")

hash = hashlib.md5(text.encode())
md5 = hash.hexdigest()

print 'The MD5 Hash of ', text, 'is', md5
