#!/usr/bin/env python3.8
from passlock import User
from passlock import Credentials


def create_new_user(username, password):
    '''
    Function that creates a new user with a username and password
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    Function that saves a new user
    '''
    user.save_user()


def display_user():
    """
    Function that  displays the existing user
    """
    return User.display_user()


def login_user(username, password):
    """
    function that checks if a user exists and thereafter logs in the user in.
    """

    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credential(account, userName, password):
    """
    Function that creates new credentials for a selected user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential


def save_credentials(credentials):
    """
    Function that  saves Credentials to the credentials list
    """
    credentials. save_details()

def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function that deletes  Credentials from credentials list

    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials of the same account
    """
    return Credentials.find_credential(account)

def check_credendtials(account):
    """
    Function that checks whether a Credentials exists with that account name and returns a boolean value

    """
    return Credentials.if_credential_exist(account)


def generate_Password():
    '''
    Function that generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):

    """
    A funct that copies the password using the pyperclip framework module
    Which is imported to declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

   




