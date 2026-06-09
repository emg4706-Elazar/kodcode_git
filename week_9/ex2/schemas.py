import mysql.connector
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    rank: str
    unit: str


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )

def get_schema():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DESCRIBE soldiers;")
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows





