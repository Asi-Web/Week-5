## Asiwome Agbleze
## CMSC 111
## Spring 2026
## Week 5 Assignment 2

def check_passwaord(password):
    if len(password) >= 8:
        return "Password acepted. It meets the minimum length requirement."
    else:
        return "Password too short. It must be at least 8 characters long."
    
## Prompt the user to enter a password
user_password = input("Enter a password: ")

## Call the function and print the result
result = check_password(user_password)
print(result)
