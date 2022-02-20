# Password-Locker
This Password-Locker project was created on 21/02/2022

## Author

[Ian Otieno](https://github.com/ian-otieno)

## Description

This project about python application that manages login and signup credentials of a person for various accounts for instance username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new password they can input password for themselves.


## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store existing acounts login details for various accounts that one have registered for.
* Generate new password for an account that one haven't registered for and store it with the account name.   
* Delete stored account login details that one do not want anymore.
* Copy one's credentials to the clipboard


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.8
* pyperclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/ian-otieno/Password-Locker.git```

* cd Password-Locker

* code . 

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py
* To run test for the application
        $ python3 passlock_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hi, Welcome to your Accounts Password Store... <br>* ca ---  Create New Account * ha ---  Have An Account |
|Select  ca| input username and password| Dear ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select ha  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```cc```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```dc```|A list of all credentials that has been stored or ```You don't have any credentials saved...``` |
|Find a stored credential based on account name|Enter ```fc```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```del```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```ex```| The application exits|

## Technologies Used

* python3.8

## Known Bugs
* There are no known bugs currently.

## Contact Information 

If you have any question or contributions, please email me at [ian.otieno@student.moringaschool.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Ian Otieno**
