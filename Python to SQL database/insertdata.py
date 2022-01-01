import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()
cursor.execute('INSERT INTO users(name,username)VALUES("Silviu","Silviu03")')
# query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
# value = ("Silviu", "Silviu03")
# cursor.execute(query, value)
# db.commit()
