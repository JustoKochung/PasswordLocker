import random
from user import User
from credentials import Credentials
from passwordGenerator import * 


# User Account Class 

def create_user(account, user_username, user_password):
    new_user = User(account, user_username, user_password)
    return new_user

def save_user(user):
    user.save_user()

# Credentials Account Class

def create_credentials(cred_account, cred_username, cred_password):
    new_credentials = Credentials(cred_account, cred_username, cred_password)
    return new_credentials

def save_credentials(credential):
    credential.save_credentials()
    
def display_credentials():
    return Credentials.display_credentials()

def delete_credentials(cred_account):
    return Credentials.delete_credentials(cred_account)

def main():
    print("Hello, welcome to Password Locker application!")
    
    while True:
        print('\n')
        print('*'*10)
        print("To navigate the application, please use shortcodes, cu to create an account, lg to login to your account, ex to exit the app")
        print('*'*10)
        
        short_code = input().lower()
        
        if short_code == 'cu':
            print("-"*15)
            print("Create an account")
            print("-"*15)
            print("Enter account name: ")
            created_account_name = input()
            print("-"*15)
            print("Welcome {{created_account_name}}. Please enter a preferred username:  ")
            print("Enter username: ")
            created_username = input()
            print("-"*15)
            
            pass_response == input("Would you prefer a generated password? Respond with y- for Yes and n- for no: ").lower()
            
            if pass_response == 'y':
                created_pass = generate_password(password_length())
                confirmed_pass = created_pass
                
                print(f"New password ({str(len(created_pass))}): -----> {created_pass}")
                
            else:
                print("Enter preferred password: ")
                created_pass = input()
                
                print("Confirm password: ")
                confirmed_pass = input()
                
                print("-"*15)
                
                print("\n")
                
                if created_pass != confirmed_pass:
                    print("Sorry, passwords do not match")
                    print("Re-enter password: ")
                    confirmed_pass = input()
                    
                else:
                    save_user(create_user(created_account_name, created_username, created_pass))
                    
                    print(f"Congratulations {created_username}, your {created_account_name} account creation was successful. ")
                    print("-"*15)
                    
                    print("Please login")
                    print("-"*15)
                    print("Enter username: ")
                    entered_username = input()
                    
                    print('Enter password: ')
                    entered_password = input()
                    
                    if entered_password != created_pass and entered_username != created_username:
                        print('Invalid username and password')
                        print('Enter username: ')
                        entered_username = input()
                        
                        print("Enter password: ")
                        entered_password = input()
                    else:
                        print('\n')
                        print(f"Welcome {entered_username}. ") 
                        print("*"*15)
        
        elif short_code == 'lg':
            print("Enter your username: ")
            default_username = input()
            
            print("Enter password: ")
            default_password = input()
            print("\n")
            
            if default_password != 'password' and default_username != 'username':
                print("Invalid: Default username is \'username\' and default password is \'password\'")       
                print("Enter username: ") 
                default_username = input()
                
                print("Enter password: ")
                default_password = input()
                
            else:
                print("Login successful!")
                print("*"*10)
                
                
                while True:
                    print("\n")
                    print("Navigate the credentials account using shortcodes : ac - add credential, lc - list credentials, and dc - delete credentials")
                    print("."*20)
                          
                
            


