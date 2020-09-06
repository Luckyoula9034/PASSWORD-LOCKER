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


def del_user(user):
    '''
    Function to delete a user detail
    '''
    user.delete_user()


def find_user(name):
    '''
    Function that finds a user by name and returns the details
    '''
    return User.find_by_name(name)
