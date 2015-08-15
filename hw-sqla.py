import csv
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    cars = csv.reader(open("inventory.csv","rU"))
    c.executemany("INSERT INTO inventory(Make,Model,Quantity)values(?,?,?)",cars)
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    print "\n Cars models and quantity in inventory\n"
    for r in rows:
        print r[0],r[1],r[2]
        
    