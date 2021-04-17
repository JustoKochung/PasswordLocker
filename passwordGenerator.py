import string
import random
    
    
def password_length():
    """Retrieves password length and returns a number 
    """
    length = input("Please input preferred password length: ")
    return int(length)

def generate_password(length=8):
    
    password = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(password)
    random_password = ''.join(random.choices(password, k=length))
    
    return random_password

   
