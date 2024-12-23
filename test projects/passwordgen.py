import random
import string

def generate_password(minLen, numbers = True, specChar = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specChar:
        characters += special
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < minLen:
        new_char = random.choice(characters)
        password+=new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number #set equal to if we have a number
        if specChar:
            meets_criteria = meets_criteria and has_special #and in case has_number is false

    return password



min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to hae special characters (y/n)? ").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)