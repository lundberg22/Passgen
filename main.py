import questionary
import random
import string

print("\n ✩⁺₊✩☽⋆ Welcome to the secure password generator ⋆☾✩⁺₊✩ \n")

#### Validate password strength, option 1 in menu
def IsValidPassword(password):

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
            if(char.islower()):
                lowerCase = True
            elif(char.isupper()):
                upperCase = True
            elif(char.isdigit()):
                number = True
            elif(not char.isalnum()):
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
        print("Would you like to see the generated password? (y/n): ")
        user_input = input().lower()
 
        if user_input in ("y", "yes"):
            print("Generated Password:", generate_password())
        else:
            print("Password lost to the depths.")

        print("New password? (y/n): ")
        retry_input = input().lower()
 
        if retry_input  in ("y", "yes"):
            print("Generated Password:", generate_password())
        else:
            print("Returning to main menu.")
            return False
        
###########################################################

#### Menu
while True:

    option = questionary.select(
    "Select an option:",
    choices=[
        "✩ Check user generated password",
        "✩ Generate a password",
        "✩ Password breach check",
        "✩ Exit"
    ]
    ).ask()

    if option == "✩ Check user generated password":
        IsValidPassword(password="")
        while True:
            userInputPassword = input("Enter your password: ")
            isValid = IsValidPassword(userInputPassword)

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

    elif option == "✩ Password breach check":
        generate_password()
        password_flow()
            
    elif option == "✩ Exit":
        print("Exiting program. Goodbye! \n")
        break

