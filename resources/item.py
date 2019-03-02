# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:45:00 2019

@author: Subham Rout
"""
from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',type = str,required = True,
                            help = "this field cannot be left blank")
    parser.add_argument('price',type = float,required = True,
                            help = "this field cannot be left blank")
    parser.add_argument('store_id',type = int,required = True,
                            help = "every item need a store id")
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return  item.json()
        return {"message": "No item found"},404
    
    @jwt_required()
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message": "the item already exists"}
        data = Item.parser.parse_args()
        
        item = ItemModel(data['name'],data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message":"A error occured inserted the item"},500  # internal server error
        
        return item.json(),201
    
    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item is deleted"}
        return {"message":"Item doesn't exist in the db"}
        
    @jwt_required()
    def put(self,name):
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(data["name"],data["price"],data['store_id'])
        else:
           item.price = data["price"]
           item.store_id = data["store_id"]
        item.save_to_db()   
        return item.json()
    
    
 
class Item_list(Resource):
     def get(self):
         return {"item": [item.json() for item in ItemModel.query.all()]}   
         
 