import time

import requests
import hashlib

import questionary
import random
import string

print("\n ✩⁺₊✩☽⋆ Welcome to the secure password generator ⋆☾✩⁺₊✩ \n")

#### Validate password strength, option 1 in menu
def is_valid_password(password):

    """Check the strength of the user's typed password.

    Criteria for success: between 8-15 characters, and at least one of each following:
    Upper case letter
    Lower case letter
    Number
    Special character
    """

    if 8 <= len(password) <= 15:
    
        lowerCase = False 
        upperCase = False
        number = False 
        specialChar = False 

        for char in password:
            if char.islower():
                lowerCase = True
            elif char.isupper():
                upperCase = True
            elif char.isdigit():
                number = True
            elif not char.isalnum():
                specialChar = True

        return lowerCase and upperCase and number and specialChar
    
    else:
        return False

##########################################################

#### Generate strong password, option 2 in menu
def generate_password(length: int = 12,
                      use_uppercase: bool = True,
                      use_lowercase: bool = True,
                      use_digits: bool = True,
                      use_special: bool = True
    )    -> str:
    """Generate a random password based on specified criteria.

    At least one of each as follows:
    - Upper case letter
    - Lower case letter
    - Number
    - Special character

    Remember to copy the password if you want to keep it.
    """
    character_pool = ""

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def password_flow() -> bool:
    while True:
        print("Generating password...")
        time.sleep(1)
        
        print("Would you like to see the generated password? (y/n): ")
        user_input = input().lower()
 
        if user_input in ("y", "yes"):
            print("\nGenerated Password: ----->", generate_password(), "<-----")
        else:
            print("Password lost to the depths.")

        print("\nNew password? (y/n): ")
        retry_input = input().lower()
 
        if retry_input  in ("y", "yes"):
            continue
        else:
            print("Returning to main menu.")
            return False
        
###########################################################

#### Password leak checker - HIBP API, option 3

"""Check if, and how many times, the provided password has been leaked online through the
haveibeenpwned.com (HIBP) API.

This code will take a user input password, turn it into a SHA-1 hash and send the first and then last part
of the hash to check whether it appears in leaked passwords. Then it will tell you if that password
has been leaked.

"""


def data_from_api(first_five_chars):
    """
    Sends the first five characters of the hashed password to HIBP API.
    Receives a list of possible password hashes that matches.
    """

    url = 'https://api.pwnedpasswords.com/range/' + first_five_chars
    result = requests.get(url)

    if result.status_code != 200:
        raise RuntimeError(f'Error: {result.status_code}. Please try again')

    return result

def leaked_password_count(result, rest_of_chars):
    """
    Receives result from the 'data_from_api' function. Sends latter part of the hashed password and sees
    if there is a match. Returns how many times the password was leaked.
    """

    hashes = [line.split(':') for line in result.text.splitlines()]
    #'h' as in 'hash' to avoid confusion
    for h, count in hashes:
        if h == rest_of_chars:
            return count
    return 0


def check_password(password):
    """
    Coverts password to SHA-1, splits into two parts. Returns leak count.

    """
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first_five_chars, rest_of_chars = hashed_password[:5], hashed_password[5:]

    result = data_from_api(first_five_chars)
    

    return leaked_password_count(result, rest_of_chars)
    
    
def password_for_you():
    password = str(input('Enter the password you want to check: '))
    leak_count = check_password(password)

    if int(leak_count) > 0:
        print(f'The password "{password}" was leaked {leak_count} times. You should probaly not use this password.')
        input("Press enter to return to menu.")
    else:
        print(f'The password "{password}" has never been leaked.')
        input("Press enter to return to menu.")

    return

###########################################################

#### Menu
while True:

    option = questionary.select(
    "Select an option:",
    choices=[
        "✩ Check user generated password",
        "✩ Generate a password",
        "✩ Check for password leaks",
        "✩ Exit"
    ]
    ).ask()

    if option == "✩ Check user generated password":
        is_valid_password(password="")
        while True:
            userInputPassword = input("Enter your password: ")
            isValid = is_valid_password(userInputPassword)

            if isValid:
                print("Strong password! \n")
                input("Press enter to return to the menu.")
                break

            elif len(userInputPassword) < 8:
                print("Password too short.")

            elif len(userInputPassword) > 15:
                print("Password too long.")

            else:
                print("Password too weak.")

            retry = input("Try again? (y/n): ").lower()
            if retry not in ("y", "yes"):
                print("Returning to menu.")
                break

    elif option == "✩ Generate a password":
        password_flow()

    elif option == "✩ Check for password leaks":
        password_for_you()
            
    elif option == "✩ Exit":
        print("Exiting program. Goodbye! ✩\n")
        break






