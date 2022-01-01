import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()
cursor.execute('CREATE TABLE users(name VARCHAR(255),username VARCHAR(255))')
