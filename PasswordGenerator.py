# Devendra-DPI

import string
import random
import secrets
import time

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''
    for _ in range(length):
        pwd += ''.join(secrets.choice(characters))
    return pwd

def password_generator_unique(length):
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(characters)
    random.shuffle(characters)
    characters_shuffle = ''.join(characters)
    return characters_shuffle[:length]

def custom_password_generator(length, custom_characters):
    characters = custom_characters + string.ascii_letters + string.digits + string.punctuation
    pwd = ''
    for _ in range(length - len(custom_characters)):
        pwd += ''.join(secrets.choice(characters))
    pwd += ''.join(custom_characters)
    return ''.join(random.sample(pwd, len(pwd)))

print("********************************\n**     PASSWORD GENERATOR     **\n********************************")
while True:
    print("\n+--------------------------------------+\
            \n| G - Contains repeated characters     |\
            \n| U - Contains unique characters       |\
            \n| C - Contains user entered characters |\
            \n| Q - Quit                             |\
            \n+--------------------------------------+")
    user_input = input("Input: ").casefold()

    try:
        if user_input == "g":
            length = int(input("Password Length: "))
            if length >= 10:
                print(f"Password ({length}): {password_generator(length)}")
            else:
                print("Password must be at least 10 characters long")
                print(f"Password (10): {password_generator(10)}")
        elif user_input == "u":
            length = int(input("Password Length: "))
            if length >= 10 and length <= 94:
                unique_pass_gen = password_generator_unique(length)
                print(f"Password ({len(unique_pass_gen)}): {unique_pass_gen}")
            elif length > 94:
                print("Unique password generator limited to 94 characters long.")
                unique_pass_gen = password_generator_unique(94)
                print(f"Password ({len(unique_pass_gen)}): {unique_pass_gen}")
            else:
                print("Password must be at least 10 characters long")
                print(f"Password (10): {password_generator_unique(10)}")
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
            time.sleep(2)
            break
        else:
            print("Enter valid inputd")
    except Exception:
        print("Enter valid input")
