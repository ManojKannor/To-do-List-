from db_conn import get_connection
def delete_Task(tableName):
    try:
        conn = get_connection()
        if conn is None:
            return 
        cursor = conn.cursor()
        task_No = int(input("Enter the delete Task NO : "))
        query = f"delete from {tableName} where no = %s"
        cursor.execute(query,(task_No,))
        conn.commit()
        print("Task deleted successfully!")
    except Exception as e:
        print("when deleting task rise a error ",e)
    finally:
        cursor.close()
        conn.close()
