import mysql.connector
from db_config import db_config
def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("connection get sucessfully")
        return conn
    except mysql.connector.Error as e:
        print("error : ",e)
        return None

    