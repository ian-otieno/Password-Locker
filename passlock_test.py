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
     
       
if __name__ == "__main__":
    unittest.main()
