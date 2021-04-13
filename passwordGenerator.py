import string
import random

class Password:
    
    def password_length():
        """Retrieves password length and returns a number
        """
        length = input("Preferred length of password: ")
        return int(length)

    def generate_password(length=8):
        
        password = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(password)
        random_password = ''.join(random.choices(password, k=length))
        
        return random_password
