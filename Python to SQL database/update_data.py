import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()
query = 'UPDATE users SET name="Vasile" WHERE id=4'
cursor.execute(query)
db.commit()
query = 'SELECT * FROM users WHERE id=4'
cursor.execute(query)
all_users = cursor.fetchall()
for user in all_users:
    print(user)
