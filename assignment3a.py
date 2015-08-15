import random
import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    
    # delete database table if exist
    c.execute("Drop TABLE if exists numbers")
    
    # create database table
    c.execute("CREATE TABLE numbers(num INT)")
    
    #insert each number into the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))