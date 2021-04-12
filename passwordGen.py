import string 
import random

def password_length():
    """Captures user preferred password length and retruns  an int.
    """
    length = input("Preferred Password length: ")
    return int(length)

def generate_password(args):
    
    
    