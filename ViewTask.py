from db_conn import get_connection
def view_task(tableName):
    try:
        conn = get_connection()
        if conn is None :
            return
        
        cursor = conn.cursor()
        cursor.execute(f"SELECT *FROM {tableName}")
        rows = cursor.fetchall()
        print(f"{'No':<6}{'TASK':<30}{'COMPLETE':<10}{'CREATED_AT':<9}")
        print("-"*59)
        for row in rows:
            created_at_str = row[3].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{row[0]:<6}{row[1]:<30}{row[2]:<10}{created_at_str:<9}")
    except Exception as e:
        print(f"when viewing data rise error : {e}")
    finally:
        cursor.close()
        conn.close()