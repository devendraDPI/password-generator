# Devendra-DPI

import string
import secrets
import time

print("********************************\n**     PASSWORD GENERATOR     **\n********************************")
while True:
    user_input = input("\nGenerate (G), Quit (Q): ").casefold()

    def password_generator(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        pwd = ''
        for i in range(length):
            pwd += ''.join(secrets.choice(characters))
        return pwd

    try:
        if user_input == "g":
            length = int(input("Password Length: "))
            if length >= 10:
                print(f"Password ({length}): {password_generator(length)}")
            else:
                print("Password must be at least 10 characters long")
                print(f"Password (10): {password_generator(10)}")
        elif user_input == "q":
            print("Thankyou :)")
            time.sleep(2)
            break
        else:
            print("Enter valid input")
    except Exception as e:
        print("Enter valid input")
