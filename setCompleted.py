from db_conn import get_connection
def setComplete(tableName):
    try:
        conn = get_connection()
        if conn is None:
            return 
        cursor = conn.cursor()
        input_no = int(input("Enter the task No : "))
        query = f"""
            UPDATE {tableName} 
            SET isdone = %s
            WHERE no = %s
        """

        cursor.execute(query,(1,input_no))
        print("Task Completed successfully")
        conn.commit()
    except Exception as e:
        print(f"when set complete use error : {e}")
    finally:
        cursor.close()
        conn.close()
