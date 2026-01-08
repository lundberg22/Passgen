import questionary

print("\n ✩⁺₊✩☽⋆ Welcome to the secure password generator ⋆☾✩⁺₊✩ \n")

#### Validate password, option 1 in menu
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
        print("Feature under development.")

    elif option == "✩ Password breach check":
        print("Feature under development.")
            
    elif option == "✩ Exit":
        print("Exiting program. Goodbye! \n")
        break
