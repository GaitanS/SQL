import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234')
cursor = db.cursor()
cursor.execute('SHOW DATABASES')

# fetchall()
databases = cursor.fetchall()  # returns a list of all databases present local
for database in databases:
    print(database)
