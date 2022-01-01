import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234')
# creating an instance of cursor class which is used executed the sql statements
cursor = db.cursor()
# creating database with the name DBPython
# execute() method used to compile a sql statement
cursor.execute('CREATE DATABASE DBPython')
