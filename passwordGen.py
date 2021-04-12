import string 
import random

def password_length():
    """Captures user preferred password length and retruns  an int.
    """
    length = input("Preferred Password length: ")
    return int(length)

def generate_password(length = 7):
    
    """Generates a random password with specific length, which defaults to 7 if nothing is specified
    """
    password = list(string.punctuation + string.ascii_letters + string.digits)
    random.shuffle(password)
    radom_password = ''.join(random.choices(password, k=length))
    return random_password

    
    