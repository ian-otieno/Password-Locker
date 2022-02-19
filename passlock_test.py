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
       
if __name__ == "__main__":
    unittest.main()
