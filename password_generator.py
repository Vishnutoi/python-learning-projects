##password generator 16 characters

import string
import random



def passwordgenerator(num):
    password = ''
    
    for x in range(num):
        x = random.randint(0,94)
        password += string.printable[x]
        
    return password

print(passwordgenerator(16))