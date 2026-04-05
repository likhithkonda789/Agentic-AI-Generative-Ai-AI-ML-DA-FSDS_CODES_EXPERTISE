import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='7893',
    auth_plugin='mysql_native_password'
)

if conn.is_connected():
    print('Connection established')

print(conn)
print(conn.is_connected())
 