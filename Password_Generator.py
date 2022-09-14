# Prints password without repeated character

import string
import random

length = int(input("Enter length: "))
chars = list(string.ascii_letters + string.digits + "*×÷$^={}\[]@#_&-+()/*:;!?,.")
password = []
random.shuffle(chars)
for i in range(20):
    ch = random.choice(chars)
    if ch not in password:
    	password.append(ch)

print("".join(password))
