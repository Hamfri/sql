import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("UPDATE inventory SET Quantity=200 WHERE Make='Fiesta'")
    c.execute("UPDATE inventory SET Model='Ford' WHERE Quantity=55")
    
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    
    for r in rows:
        print r[0],r[1],r[2]