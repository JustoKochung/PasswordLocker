import pyperclip

class User:
    """
    Class that generates new instances of a user
    """
    userList = [] # Empty user list
    
    def __init__(self, userName, password):
        """Function to create a new instance of credentials
        """
        self.userName = userName
        self.password = password
        
    def saveUser(self):
        
        """Function to store credentials
        """
        User.userList.append(self)
    
    def deleteUser(self): 
        
        """Function to delete credentials
        """
        User.userList.remove(self)
    
    def display_user():
        """Function to display all credentials
        """
        return User.userList()
    
@classmethod
    def find_credentials_by_userName(cls, userName): 
        """Function to find user credentials 
        """
        for credentials in cls.userList:
            if credentials.userName == userName
            return credentials
        
        
@classmethod
    def copy_password(cls, password):
        """Function to copy password
        """
        password_found = User.find_credentials_by_userName(password)
        pyperclip.copy(password_found.password)

@classmethod
    def copy_userName(cls, userName):
        """Function to copy username
        """
        username_found = User.find_credentials_by_userName(userName)
        pyperclip.copy(username_found.userName)
        
        
    
    
        