import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Use your MySQL username
    password='7893',
    auth_plugin='mysql_native_password',
    database='pythondb'  # Correct DB name
)

mycursor = conn.cursor()

sql = 'INSERT INTO student (name, branch, id) VALUES (%s, %s, %s)'

val = [
    ('john', 'cse', 56),
    ('mike', 'ece', 57),
    ('sara', 'mech', 58)
]

mycursor.executemany(sql, val)
conn.commit()

print(mycursor.rowcount, 'records inserted')
