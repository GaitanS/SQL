# connecting to the database


import mysql.connector as mysql

# connecting to the database using connect() method
# 3 parameters host, user, password

db = mysql.connect(host='localhost', user='root', password='Frectie!234')
print(db)
