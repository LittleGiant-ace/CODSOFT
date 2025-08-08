import random
import string

print("Welcome to Password Generator")
print("\nChoose character types:")
print("1 = Lowercase (a-z)")
print("2 = Uppercase (A-Z)")
print("3 = Digits (0-9)")
print("4 = Symbols (!@#$%...)")

length_input = input("\nEnter desired password length: ")
types_input = input("Enter any combination (like 123 or 14): ")

if not length_input.isdigit():
    print("Error: Length must be a number.")
    exit()

length = int(length_input)
if length < 4:
    print("Error: Password should be at least 4 characters long.")
    exit()

char_pool = ""

if '1' in types_input:
    char_pool += string.ascii_lowercase
if '2' in types_input:
    char_pool += string.ascii_uppercase
if '3' in types_input:
    char_pool += string.digits
if '4' in types_input:
    char_pool += string.punctuation

if not char_pool:
    print("Error: No valid character types selected.")
    exit()

password = ''.join(random.choice(char_pool) for _ in range(length))

print("\nYour generated password is:")
print(password)

import pyperclip  # Add this at the top with other imports

pyperclip.copy(password)
print("\nThe password has been copied to your clipboard.")
