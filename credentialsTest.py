import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """Test class that defines test cases for the credentials class behaviors

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    
    def setUp(self):
        """Set up method to run before each test cases
        """
        self.new_credentials = Credentials("Justo", "0799762744") # New Credentials objects
        
    def test_init(self):
        self.assertEqual(self.new_credentials.cred_username, "Justo")
        self.assertEqual(self.new_credentials.cred_password, "0799762744")
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials() #saving new credentials
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        Credentials.credentials_list = []
    
    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Ochung", "0712351762")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
        
if __name__ == '__main__':
    unittest.main()
    
        