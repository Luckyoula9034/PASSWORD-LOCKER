import unittest  # Importing the unittest module
from user import User  # Importing the credential class

class TestUser(unittest.TestCase):
     '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    
    '''

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = User(
            "lucky", "oula", "0759099034", "luckyoula@gmail.com")  # create credential object