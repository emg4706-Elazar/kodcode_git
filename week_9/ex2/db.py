import mysql.connector
import uvicorn

from main import post_soldier


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )


def get_all():
    conn = get_connection()
    sql_query = """
    SELECT * FROM soldiers;
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_by_id(soldier_id: int):
    conn = get_connection()
    sql = """
        SELECT * FROM soldiers WHERE (id) = (%s);
        """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (soldier_id,))
    row = cursor.fetchone()
    conn.close()
    cursor.close()
    return row


def create(name, rank, unit):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    INSERT INTO soldiers (name, mrank, unit) 
    VALUES (%s, %s, %s);
    """
    values = (name, rank, unit)
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    cursor.close()
    return new_id


def update(soldier_id, data: dict):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    UPDATE soldiers
    SET name = %s, mrank = %s, unit = %s
    WHERE id = %s;
    """
    values = (data["name"], data["rank"], data["unit"],soldier_id)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    cursor.close()
    return f"success"



def delete(soldier_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    DELETE FROM soldiers WHERE id = (%s);
    """
    cursor.execute(sql, (soldier_id,))
    conn.commit()# how to check if the column changed
    deleted = cursor.rowcount
    conn.close()
    cursor.close()
    return deleted


if __name__ == "__main__":
    name1 = "David"
    rank1 = "sergeant"
    unit1 = "8200"
    data1 = {"name": "David", "rank": "sergeant", "unit": "8200"}


    print(get_all())
    create(name1, rank1, unit1)
    print(get_all())




