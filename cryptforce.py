#!/usr/bin/python

import crypt
from termcolor import colored

def crackPass(cryptWord):
    salt = cryptWord[0:2] #First two letter of our crypt
    dictionary = open("dictionary.txt", 'r')
    for word in dictionary.readlines():
            word = word.strip('\n')
            cryptPass = crypt.crypt(word,salt)
            if cryptWord == cryptPass:
                print(colored("[+] Found Password: " +  word, 'green'))
                exit(0)
                
    print(colored("[-] Password Not Found!", 'red'))
    


def main():
    passFile = open('cryptpass.txt','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip(' ').strip('\n') #Always remove new line, as it will cause less problem
            print("[*] Cracking Password For: " + user)
            crackPass(cryptWord)

main()
