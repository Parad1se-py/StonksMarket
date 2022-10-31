from the_big_username_blacklist import validate
from validate_email import validate_email

def email_validator(email: str) -> list:
    if validate_email(email, verify=True):
        return [True]
    else:
        return [False, "Please enter a valid email"]

def pass_validator(password: str) -> list:
    if len(password) < 8:
        return [False, "Please enter a password with length greater than 8 characters."]

def username_validator(username: str) -> list:
    if len(username) < 4:
        return [False, "Please enter a username with length greater than 3 characters."]

    if not validate(username):
        return [False, "That username is not allowed. Please choose another username."]
