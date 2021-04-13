import unittest # Importing the unittest module
from user import User # Importing the User class

class TestUser(unittest.TestCase):
    """Test Class for defining test cases for user class behaviours 

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    
    def setUp(self):
        """Set up method to run before each test cases.
        """
        self.new_user = User("Justo", "Ochung", "lK7HR,0Op") # Create user object
        
    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.account, "Justo") #TestCase method that checks for an expected result
        self.assertEqual(self.new_user.user_username, "Ochung")
        self.assertEqual(self.new_user.user_password, "lK7HR,0Op")
        
        
if __name__ == " __main__ " :
    unittest.__main__()
    