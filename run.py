#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(f_name, l_name, password, email):
    '''
    Function to create a new user
    '''
    new_user = User(f_name, l_name, password, email)
    return new_user
    

def save_users(user):
    '''
    Function to save user detail
    '''
    user.save_user()
