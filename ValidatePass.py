def IsValidPassword(password):
    """Check if the provided password meets the required criteria.

    Criteria:
    - At least 8 characters long, but no more than 15 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character

    Args:
        password (str): The password string to validate.
    Returns:
        bool: True if the password is valid, False otherwise.   
    """
    if 8 <= len(password) <= 15:
    
        lowerCase = False 
        upperCase = False
        digit = False 
        specialChar = False 

        for char in password:
            if(char.islower()):
                lowerCase = True
            elif(char.isupper()):
                upperCase = True
            elif(char.isdigit()):
                digit = True
            elif(not char.isalnum()): # Checks if it's NOT a number or letter = it's a special character
                specialChar = True

        return lowerCase and upperCase and digit and specialChar
    
    else:
        return False

while True:
    userInputPassword = input("Enter your password: ")
    isValid = IsValidPassword(userInputPassword)

    if isValid:
        print("Strong password")
        break

    elif len(userInputPassword) < 8:
        print("Password too short")

    elif len(userInputPassword) > 15:
        print("Password too long")

    else:
        print("Password too weak")

    retry = input("Do you want to try again? (y/n): ").lower()
    if retry not in ("y", "yes"):
        print("Exiting password checker. Goodbye!")
        break
