#!/usr/bin/env python3.8
from passlock import User
from passlock import Credentials
import pyperclip


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
    A function that copies the password using the pyperclip framework module
    Which is imported to declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

def passwordlocker():
    print("Hi Welcome to your Accounts Password Store...\n Please enter one of the following to continue.\n ca ---  Create a New Account  \n ha ---  Have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 60)
        username = input("User_name: ")
        while True:
            print(" tp - To type your own pasword:\n gp - To generate your random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username, password))
        print("*"*90)
        print(
            f"Dear {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*90)

    elif short_code == "ha":
        print("*"*60)
        print("Enter your User name and your Password to log in:")
        print('*' * 60)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Dear {username}.Welcome To  your PassWord Locker Manager")
            print('\n')
   

if __name__ == '__main__':
    passwordlocker()
   

   




