import pymysql
import pandas as pd

def view_data():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Vivek@807',
            db='cv'
        )
        
        print("\n--- TABLES IN DATABASE 'CV' ---")
        tables = pd.read_sql("SHOW TABLES", connection)
        print(tables)
        print("\n" + "="*50 + "\n")

        # Check user_data
        if 'user_data' in tables.values:
            print("--- CONTNETS OF 'user_data' TABLE ---")
            df_users = pd.read_sql("SELECT * FROM user_data", connection)
            if df_users.empty:
                print("[Table is empty]")
            else:
                print(df_users.head()) # Show first 5 rows
            print("\n" + "="*50 + "\n")

        # Check user_feedback
        if 'user_feedback' in tables.values:
            print("--- CONTENTS OF 'user_feedback' TABLE ---")
            df_feed = pd.read_sql("SELECT * FROM user_feedback", connection)
            if df_feed.empty:
                print("[Table is empty]")
            else:
                print(df_feed.head())
            print("\n" + "="*50 + "\n")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

if __name__ == "__main__":
    view_data()
