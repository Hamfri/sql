import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    sql = {'Ford': "SELECT COUNT(Make) FROM orders WHERE Model='Ford'",
           'Honda': "SELECT COUNT(Make) FROM orders WHERE Model='Honda'",
           'Subaru': "SELECT COUNT(Make) FROM orders WHERE Model='Subaru'",
           'Mazda': "SELECT COUNT(Make) FROM orders WHERE Model='Mazda'",
           'Toyota': "SELECT COUNT(Make) FROM orders WHERE Model='Toyota'"
           }
    
    for keys, values in sql.iteritems():
        c.execute(values)
        
        result = c.fetchone()
        print keys + ":", result[0]