# Devendra-DPI

import string
import random
import secrets
import time

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''
    for i in range(length):
        pwd += ''.join(secrets.choice(characters))
    return pwd

def custom_password_generator(length, custom_characters):
    characters = custom_characters + string.ascii_letters + string.digits + string.punctuation
    pwd = ''
    for i in range(length - len(custom_characters)):
        pwd += ''.join(secrets.choice(characters))
    pwd += ''.join(custom_characters)
    return ''.join(random.sample(pwd, len(pwd)))

print("********************************\n**     PASSWORD GENERATOR     **\n********************************")
while True:
    print("\n+------------------------------+\n|   Generate (G), Custom (C)   |\n|   Quit (Q)                   |\n+------------------------------+")
    user_input = input("Input: ").casefold()

    try:
        if user_input == "g":
            length = int(input("Password Length: "))
            if length >= 10:
                print(f"Password ({length}): {password_generator(length)}")
            else:
                print("Password must be at least 10 characters long")
                print(f"Password (10): {password_generator(10)}")
        elif user_input == "c":
            custom_characters = input("Enter characters to be in password: ")
            length = int(input("Password Length: "))
            if length >= 10:
                print(f"Password ({length}): {custom_password_generator(length, custom_characters)}")
            else:
                print("Password must be at least 10 characters long")
                print(f"Password (10): {custom_password_generator(10, custom_characters)}")
        elif user_input == "q":
            print("Thankyou :)")
            time.sleep(3)
            break
        else:
            print("Enter valid input")
    except Exception as e:
        print("Enter valid input")
