import unittest # importing the unittest module
from Credential import Credential #importint the credential class

class TestCredential(unittest.TestCase):

        """
        Test class that defines test cases for the credential class behaviours.
    
        Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    
        """
def setup(self):

        """
        test_init test case to test if the object is initialized properly
    
        """

        self.new_Credential = Credential("Lucky","Oula","0759099034","luckyoula@gmail.com")



def test_init(self):

        """
        test_init test case to test if the object is initialized properly
    
        """
    
        self.assertEqual(self.new_credential_name,"lucky")
        self.assertEqual(self.new_user_name,"oula")
        self.assertEqual(self.new_password,"0759099034")
        self.assertEqual(self.new_email,"luckyoula@gmail.com")


if __name__ =='__main__':
    unittest.main()
