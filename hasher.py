#!/usr/bin/python

'''
Inputting passwords into different hashing algorithms: MD5, SHA1, SHA224, SHA245, SHA256
'''

import hashlib #Performs hashes package
from termcolor import colored

hashvalue = input("[*] Enter a string to hash: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print("[+] Password in MD5 hash is: " + colored(hashobj1.hexdigest(),'green'))

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print("[+] Password in SHA1 hash is: " + colored(hashobj2.hexdigest(),'green'))

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print("[+] Password in SHA224 hash is: " +colored( hashobj3.hexdigest(),'green'))

hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print("[+] Password in SHA256 hash is: " + colored(hashobj4.hexdigest(),'green'))

hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print("[+] Password in SHA256 hash is: " + colored(hashobj5.hexdigest(),'green')) 
