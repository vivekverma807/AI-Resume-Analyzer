
import streamlit as st
import pymysql

# Get connection details as inputs
st.title("TiDB Cloud Setup Tool")
st.write("Use this tool to initialize your TiDB Cloud database.")

with st.form("db_setup"):
    host = st.text_input("TiDB Host (e.g., gateway01...tidbcloud.com)")
    port = st.number_input("Port", value=4000)
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Initialize Database")

if submit:
    try:
        # 1. Connect to default database first to create 'cv'
        conn = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            ssl={"ssl_mode": "VERIFY_IDENTITY"} # Important for TiDB!
        )
        cursor = conn.cursor()
        
        # Create Database
        st.info("Creating database 'cv'...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS cv;")
        cursor.execute("USE cv;")
        
        # Create user_data table
        st.info("Creating table 'user_data'...")
        table_sql = """CREATE TABLE IF NOT EXISTS user_data (
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
        );"""
        cursor.execute(table_sql)

        # Create user_feedback table
        st.info("Creating table 'user_feedback'...")
        tablef_sql = """CREATE TABLE IF NOT EXISTS user_feedback (
            ID INT NOT NULL AUTO_INCREMENT,
            feed_name varchar(50) NOT NULL,
            feed_email VARCHAR(50) NOT NULL,
            feed_score VARCHAR(5) NOT NULL,
            comments VARCHAR(100) NULL,
            Timestamp VARCHAR(50) NOT NULL,
            PRIMARY KEY (ID)
        );"""
        cursor.execute(tablef_sql)
        
        conn.commit()
        st.success("✅ Database 'cv' and tables created successfully!")
        st.balloons()
        
    except Exception as e:
        st.error(f"Error: {e}")
