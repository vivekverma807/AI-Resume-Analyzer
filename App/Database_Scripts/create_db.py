import pymysql

# Connect to MySQL Server (no specific database yet)
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Vivek@807'
    )
    cursor = connection.cursor()
    
    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS cv")
    
    print("Database 'cv' created successfully (or already exists).")
    
    # Verify it exists
    cursor.execute("SHOW DATABASES LIKE 'cv'")
    result = cursor.fetchone()
    if result:
        print(f"Verified: Database '{result[0]}' is present.")
    
except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
