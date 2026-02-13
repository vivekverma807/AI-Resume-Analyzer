
import streamlit as st
import pymysql

# Get connection details as inputs
st.title("TiDB Cloud/Local DB Cleaner")
st.write("Use this tool to **WIPE** all data from your database (Fresh Start).")
st.warning("⚠️ This action cannot be undone!")

with st.form("db_setup"):
    host = st.text_input("Host (e.g., gateway01...tidbcloud.com or localhost)", value="gateway01.eu-central-1.prod.aws.tidbcloud.com")
    port = st.number_input("Port", value=4000)
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    db_name = st.text_input("Database Name", value="cv")
    submit = st.form_submit_button("🗑️ CLEAR ALL DATA")

if submit:
    try:
        # Connect to database
        conn = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            # Handle SSL only if not localhost
            ssl={"ssl_mode": "VERIFY_IDENTITY"} if host != "localhost" else None
        )
        cursor = conn.cursor()
        
        st.info(f"Connected to '{db_name}'. Clearing tables...")

        # TRUNCATE deletes all rows but keeps the table structure (faster than DELETE)
        try:
            cursor.execute("TRUNCATE TABLE user_data;")
            st.success("✅ Table 'user_data' cleared.")
        except Exception as e:
            st.warning(f"Could not clear 'user_data': {e}")

        try:
            cursor.execute("TRUNCATE TABLE user_feedback;")
            st.success("✅ Table 'user_feedback' cleared.")
        except Exception as e:
            st.warning(f"Could not clear 'user_feedback': {e}")
        
        conn.commit()
        st.balloons()
        st.success("🎉 Database is now fresh and empty!")
        
    except Exception as e:
        st.error(f"Error: {e}")
