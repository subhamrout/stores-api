# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:39:35 2019

@author: Subham Rout
"""

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"Message":"Store Not found"},404
        
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"Message":"A store with name '{}' already exists".format(name)},400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {"Message": "A error occured while creating the store"},500
        return store.json(),201    
    
    def delete(self,name):
        store =  StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message":"store is deleted"}
        return {"Message":"Store doesn't exist in the database for deletion"}
    
class StoreList(Resource):
     def get(self):
         return {"stores":[store.json() for store in StoreModel.query.all()]}