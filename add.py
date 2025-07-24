from db_conn import get_connection

def add(tableName):
    try:
        conn = get_connection()
        if conn is None:
            return
        
        
        cursor = conn.cursor()
        task_value = input("Enter the Task : ")
        query = f"INSERT INTO {tableName}(task) values(%s)"
        cursor.execute(query,(task_value,))
        conn.commit()
        print("Task is Added")
    except Exception as e:
        print(f"when adding the task rise error : {e}")
    finally:
        cursor.close()
        conn.close()

