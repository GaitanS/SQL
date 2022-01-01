import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()
cursor.execute('SHOW TABLES')

# fetchall()
tables = cursor.fetchall()  # returns a list of all databases present local
for table in tables:
    print(table)
