import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()
cursor.execute('DROP TABLE users')  # stergem tabela users din baza de date
cursor.execute(
    'CREATE TABLE users(id INTEGER(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,name VARCHAR(255),username VARCHAR('
    '255))')
# deleted ID cloumn
cursor.execute('ALTER TABLE users DROP id')
# adding id column to the users table
# 'first' keyword in the stamnent will add a column in the start of the table
cursor.execute('ALTER TABLE users ADD COLUMN id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST')

cursor.execute('DESC users')

print(cursor.fetchall())
