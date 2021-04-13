
class User:
    """Class that generates new instances of users
    """
    user_list = [] #Empty user list
    
    def __init__(self, account, user_username, user_password):
        
        """New instance variables (account, password, and username)of the class
        """
        self. account = account
        self. user_username = user_username
        self.user_password = user_password
        
    def save_user(self):
        """Method to save user objects into user_list
        """
        User.user_list.append(self)
    
    def delete_user(self):
        """Method that deletes a saved user from the user list
        """
        User.user_list.remove(self)
        
        
        
    
    
        