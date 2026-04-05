import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='7893',
    auth_plugin='mysql_native_password'
)

if conn.is_connected():
    print('connection established')

mycursor = conn.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS pythondb')
print("Database checked/created successfully!")
