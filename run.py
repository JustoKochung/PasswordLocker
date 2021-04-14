import random
from user import User
from credentials import Credentials
from passwordGenerator import Password

def create_user(account, user_username, user_password):
    """Function to create a new user

    Args:
        account ([account]): [New User account]
        user_username ([username]): [New User username]
        user_password ([password]): [New User password]
    """
    new_user = User(account, user_username, user_password)
    return new_user

def save_user(user):
    """Function to save user
    """
    user.save_user()

def create_credentials(cred_username, cred_password):
    new_credentials = Credentials(cred_username, cred_password)
    return new_credentials
def save_credentials(credentials):
    credentials.save_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def display_credentials():
    return Credentials.display_credentials()


def main():
    print("Hello, Welcome to Password Locker Application!. What is your name?")
        user_name = input()
        
        print(f"Hello {{user_name}}. What would you like to do? ")
        print('\n')
        
        while True:
            print("Use these shortcodes to navigate the application: cu- to create app account, lg- to login in as new user, ex- to exit the app )
            print ("-"*10)
            
            short_code = input().lower()
            
            if short_code == 'cu':
                print("New Application User, Please go ahead and create an account")
                print('-'*15)
                print("Please enter a the user account name i.e Twitter, Instangram, gmail etc: ")
                account = input()
                user_username = input("Enter preferred username: ")
                print("."*10)
                
                password_generator = input("Use shortcodes 'y' for application generated password or 'n' to choose your preferred password"
                ).lower()
                
                if password_generator == 'y':
                    pass_created = generate_password(password_length())
                    pass_confirmed = pass_created
                    
                
                  
    