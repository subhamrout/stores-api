# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:21:36 2019

@author: Subham Rout
"""

from models.user import UserModel
from  werkzeug.security import safe_str_cmp

def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user != None and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

    
        