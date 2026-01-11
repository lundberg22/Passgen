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
import random
import string
import time
import requests
import hashlib
import questionary
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
  
## Screenshots
1. <img width="416" height="134" alt="1" src="https://github.com/user-attachments/assets/d9c7d4dc-a66c-48e3-a8cc-62d42911c43f" />

2. <img width="356" height="147" alt="2" src="https://github.com/user-attachments/assets/7603cc35-8755-451f-8aef-7229992ed5a9" />

3. <img width="302" height="123" alt="3" src="https://github.com/user-attachments/assets/8f8066d1-852d-49f9-ab2d-52dc61c15541" />

4. <img width="395" height="86" alt="4" src="https://github.com/user-attachments/assets/e43f2abc-932d-4c8f-bf20-a776f5dae3fa" />

5. <img width="373" height="142" alt="5" src="https://github.com/user-attachments/assets/9880347f-2ceb-4ff5-8a31-2caec6978ce5" />

6. <img width="380" height="170" alt="6" src="https://github.com/user-attachments/assets/aaab74d0-7c1f-4217-b332-88ae67c00f9c" />

7. <img width="660" height="80" alt="7" src="https://github.com/user-attachments/assets/6e8bc56a-5685-4d2d-8060-94a0a131ae88" />

8. <img width="351" height="83" alt="8" src="https://github.com/user-attachments/assets/b795dce9-a2fa-4aa7-91bb-c0f4d99e9eaa" />

## Flowchart
<img width="1297" height="909" alt="flowchart" src="https://github.com/user-attachments/assets/60472791-b1dc-4086-8f75-a38ecea4d3e9" />

## Disclaimer
This program is created for educational purposes. While functional, it can be further developed and polished into a better version later down the line.
