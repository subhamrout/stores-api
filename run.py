# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:33:35 2019

@author: Subham Rout
"""

from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_all():
    db.create_all()