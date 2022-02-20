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


