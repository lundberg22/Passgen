# Password checker and generator

## Description

This project aims to create a script for password generation as well as strength validation and checking.
The goal of this is to facilitate the password generation process for the user through a strength checker as well as checking against known leaks through HIBP, while also ensuring the password is difficult to crack.

## Requirements
### Installation from terminal:
```
python -m pip install questionary
```
```
pip install requests
```

For modules to work.
### Modules:
```
import requests
import hashlib
import questionary
import random
import string
```

### General requirements
- Any OS
- Python 3.x

## How to use
Run the program in python. Choose what you would like to do from the options in the menu by using arrow keys.
### Options
1. Check strength of password
   - The user types in a password and the program returns a response on strength
2. Generate a password
   - The program generates a strong password based on specific criteria
3. Password breach check
   - The user types in a password and the program checks if it has been in any known leaks
  
## Screenshot/video
Coming soon

## Flowchart
Coming soon

## Disclaimer
This program is created for educational purposes. While functional, it can be further developed and polished into a better version later down the line.
