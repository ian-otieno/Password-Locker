#!/usr/bin/env python3.8
import unittest
from passlock import User
from passlock import Credentials

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('IanOtieno','YxR4t1')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'IanOtieno')
        self.assertEqual(self.new_user.password,'YxR4t1')

    def test_save_user(self):
        """
        test case that tests if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        """
        Method that runs prior to each individual credentials test methods run.

        """
        self.new_credential = Credentials('Gmail','Ian_Otieno','db4Knp')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'Ian_Otieno')
        self.assertEqual(self.new_credential.password,'db4Knp')

    def save_credential_test(self):
        """
        test case to test whether the crential object is saved into the credentials list.

        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Facebook","ianotieno","Sd6mL3") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

       
if __name__ == "__main__":
    unittest.main()
