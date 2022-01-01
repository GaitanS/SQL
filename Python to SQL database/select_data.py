import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()

# query = 'SELECT * FROM users'
# query = 'SELECT username FROM users WHERE ID = 5'
# query = 'SELECT * FROM users ORDER BY name'
query = 'SELECT * FROM users ORDER BY name ASC'
cursor.execute(query)
all_users = cursor.fetchall()
for user in all_users:
    print(user)


