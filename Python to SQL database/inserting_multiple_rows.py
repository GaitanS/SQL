import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='DBPython')
cursor = db.cursor()
# defining the query
query = 'INSERT INTO users(name,username)VALUES(%s,%s)'

values = [
    ('Silviu', 'siliu01'),
    ('Silviu1', 'siliu02'),
    ('Silviu2', 'siliu03'),
]
# executing the query with values
cursor.executemany(query, values)
db.commit()

print(cursor.rowcount, 'records_inserted')
