# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:20:29 2019

@author: Subham Rout
"""

from flask_restful import Resource,reqparse 
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type = str
                            ,required = True,help = "This field cannot be left blank")
    parser.add_argument('password',type = str
                            ,required = True,help = "This field cannot be left blank")
        ##data = parser.parse_args()
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"A User with that username already exists"},400
        user = UserModel(**data)
        user.save_to_db()
        
        return {"message": "The user registertion sucessful"},201
        
    


























      