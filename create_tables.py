# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:05:12 2019

@author: Subham Rout
"""

import sqlite3

connection  = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table  = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY , username text,password text)"

cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text, price real)" 
cursor.execute(create_table)




connection.commit()
connection.close()
