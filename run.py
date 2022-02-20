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



