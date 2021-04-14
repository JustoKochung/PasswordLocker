import pyperclip

class Credentials:
    """Class that generates new instances of credentials
    """
    credentials_list = [] # Empty credentials list
    
    def __init__(self, cred_account, cred_username, cred_password):
        """__init__ method that helps define properties for our objects.

        Args:
            cred_username : New Credential username
            cred_password : New credential password
        """
        self.cred_account = cred_account 
        self.cred_username = cred_username
        self.cred_password = cred_password
        
    def save_credentials(self):
        Credentials.credentials_list.append(self)
    
    @classmethod
    def delete_credentials(cls, cred_account):
       for credential in cls.credentials_list:
           if credential.cred_account == cred_account:
               cls.credentials_list.remove(credential)
    
    # @classmethod
    # def find_credentials_by_username(cls,cred_username):
        
    #     for credentials in cls.credentials_list:
    #         if credentials.cred_username == cred_username:
    #             return credentials
    
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
    
 