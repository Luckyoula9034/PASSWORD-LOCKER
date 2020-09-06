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

def test_init(self):

    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.account_name, "lucky")
    self.assertEqual(self.new_user.user_name, "oula")
    self.assertEqual(self.new_user.password, "0759099034")
    self.assertEqual(self.new_user.email, "luckyoula@gmail.com")
def test_save_user(self):
    '''
    test_save_user test case to test if the credential object is saved into
     the user list
    '''
    self.new_user.save_user()  # saving the new user
    self.assertEqual(len(User.user_list), 1)
def tearDown(self):

    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

def test_save_multiple_users(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test", "lucky", "0759099034",
                                     "luckyoula@gmail.com")  # new contact
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
def test_delete_user(self):
        '''
        test_delete_credential to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User(
            "Test", "lucky", "0759099034", "luckyoula@gmail.com")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)
