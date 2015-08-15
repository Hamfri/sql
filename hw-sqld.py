import csv
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    orders = csv.reader(open("orders.csv","rU"))
    
    c.execute("CREATE TABLE orders(make TEXT,model TEXT,order_date DATE)")
    c.executemany("INSERT INTO orders(make,model,order_date)VALUES(?,?,?)",orders)
    
    c.execute("SELECT inventory.Make,orders.model,inventory.Quantity,orders.order_date FROM inventory,orders WHERE inventory.Make=orders.make")
    rows = c.fetchall()
    for r in rows:
        print"Make: {} Model: {}".format(r[0],r[1])
        print "Quantity: " + str(r[2])
        print "Order date: {}".format(r[3])
        print
    
    