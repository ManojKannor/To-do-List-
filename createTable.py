from db_conn import get_connection
def create_Table(tableName):
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {tableName}(No INT AUTO_INCREMENT PRIMARY KEY,
                                    Task VARCHAR(30),
                                    isdone boolean DEFAULT FALSE,
                                    created_at timestamp DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("table is created")
    except Exception as e:
        print("table creating error : ",e)
    finally:
        if conn:
            cursor.close()
            conn.close()



