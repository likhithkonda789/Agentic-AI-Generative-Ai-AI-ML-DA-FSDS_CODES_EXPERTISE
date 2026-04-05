import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',        # Use your MySQL username
    password='7893', 
    auth_plugin='mysql_native_password',# Use your MySQL password
    database='pythondb' # Database must already exist
)

if conn.is_connected():
    print("Connection established")

# Create cursor
mycursor = conn.cursor()

# Create table (correct syntax)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        name VARCHAR(50),
        branch VARCHAR(20),
        id INT
    )
""")

# Show tables
mycursor.execute("SHOW TABLES")

# Print tables
for table in mycursor:
    print(table)
