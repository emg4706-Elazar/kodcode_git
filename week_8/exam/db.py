import mysql.connector

def get_connection():
    return mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="secret",
                database="mydb")


def get_schema():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE weapons")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{ "id": row[0], "name": row[1]} for row in rows]
