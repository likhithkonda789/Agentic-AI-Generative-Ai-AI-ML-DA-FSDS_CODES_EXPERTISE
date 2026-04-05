import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='7893',auth_plugin='mysql_native_password')

mycursor = conn.cursor()
mycursor.execute('show databases')

for x in mycursor:
    print(x)    