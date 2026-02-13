import pymysql

# Connect to MySQL Server (Localhost default)
try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Vivek@807',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    
    # 1. Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS cv")
    print("Database 'cv' checked/created.")
    
    # Select the database
    connection.select_db('cv')

    # 2. Create user_data table
    table_user = """
    CREATE TABLE IF NOT EXISTS user_data (
        ID INT NOT NULL AUTO_INCREMENT,
        sec_token varchar(20) NOT NULL,
        ip_add varchar(50) NULL,
        host_name varchar(50) NULL,
        dev_user varchar(50) NULL,
        os_name_ver varchar(50) NULL,
        latlong varchar(50) NULL,
        city varchar(50) NULL,
        state varchar(50) NULL,
        country varchar(50) NULL,
        act_name varchar(50) NOT NULL,
        act_mail varchar(50) NOT NULL,
        act_mob varchar(20) NOT NULL,
        Name varchar(500) NOT NULL,
        Email_ID VARCHAR(500) NOT NULL,
        resume_score VARCHAR(8) NOT NULL,
        Timestamp VARCHAR(50) NOT NULL,
        Page_no VARCHAR(5) NOT NULL,
        Predicted_Field BLOB NOT NULL,
        User_level BLOB NOT NULL,
        Actual_skills BLOB NOT NULL,
        Recommended_skills BLOB NOT NULL,
        Recommended_courses BLOB NOT NULL,
        pdf_name varchar(50) NOT NULL,
        PRIMARY KEY (ID)
    );
    """
    cursor.execute(table_user)
    print("Table 'user_data' checked/created.")

    # 3. Create user_feedback table
    table_feedback = """
    CREATE TABLE IF NOT EXISTS user_feedback (
        ID INT NOT NULL AUTO_INCREMENT,
        feed_name varchar(50) NOT NULL,
        feed_email VARCHAR(50) NOT NULL,
        feed_score VARCHAR(5) NOT NULL,
        comments VARCHAR(100) NULL,
        Timestamp VARCHAR(50) NOT NULL,
        PRIMARY KEY (ID)
    );
    """
    cursor.execute(table_feedback)
    print("Table 'user_feedback' checked/created.")
    
    print("\n✅ Database setup complete successfully!")

except pymysql.MySQLError as e:
    print(f"❌ Error connecting to MySQL: {e}")
    print("Please ensure MySQL is running and credentials ('root' / 'Vivek@807') are correct.")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
