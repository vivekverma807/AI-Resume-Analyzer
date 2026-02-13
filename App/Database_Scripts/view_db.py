
import streamlit as st
import pymysql
import pandas as pd

# Page Configuration
st.set_page_config(page_title="DB Viewer", layout="wide")

# Get connection details as inputs
st.title("TiDB Cloud/Local DB Viewer")
st.write("Use this tool to **VIEW** all data from your database (Cloud or Local).")

with st.sidebar.form("db_setup"):
    st.subheader("Database Connection")
    host = st.text_input("Host", value="gateway01.eu-central-1.prod.aws.tidbcloud.com")
    port = st.number_input("Port", value=4000)
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    db_name = st.text_input("Database Name", value="cv")
    submit = st.form_submit_button("Connect & View")

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
        
        st.success(f"Connected to '{db_name}' successfully!")

        # 1. Show Tables
        st.header(f"Tables in '{db_name}'")
        tables_df = pd.read_sql("SHOW TABLES;", conn)
        st.dataframe(tables_df)

        # 2. View User Data
        st.divider()
        st.header("📋 User Data (user_data)")
        try:
            df_users = pd.read_sql("SELECT * FROM user_data;", conn)
            if df_users.empty:
                st.warning("Table 'user_data' is empty.")
            else:
                st.dataframe(df_users)
                st.info(f"Total Rows: {len(df_users)}")
        except Exception as e:
            st.error(f"Could not read 'user_data': {e}")

        # 3. View User Feedback
        st.divider()
        st.header("💬 User Feedback (user_feedback)")
        try:
            df_feed = pd.read_sql("SELECT * FROM user_feedback;", conn)
            if df_feed.empty:
                st.warning("Table 'user_feedback' is empty.")
            else:
                st.dataframe(df_feed)
                st.info(f"Total Rows: {len(df_feed)}")
        except Exception as e:
            st.error(f"Could not read 'user_feedback': {e}")
        
    except Exception as e:
        st.error(f"Connection Error: {e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()
