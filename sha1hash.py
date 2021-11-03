#!/usr/bin/python

'''
This code cracks SHA1 Hashed passwords from an online dictionary, github 10mil password
'''

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input("[*] Enter Sha1 Hash Value: ")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8') # Reading the raw git hub and websites are encoded utf-8

for i in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(i, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored("[+] The Password is: " + str(i),'green'))
        quit()
    else:
        print(colored("[-] Passsword guess " + str(i) + "does not match, trying next...",'red'))

print("Password not in passwordList")
