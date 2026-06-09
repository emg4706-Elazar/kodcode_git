from db import get_connection


def get_by_rank(rank):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM soldiers WHERE mrank = %s;"
    cursor.execute(sql, (rank,))
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_active_sorted(order = "asc"):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if order.lower() not in ("asc", "desc"):
        order = "asc"
    sql = f"SELECT * FROM soldiers WHERE active = TRUE ORDER BY name {order.upper()};"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows


def search_by_name(term):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM soldiers WHERE name LIKE %s;"
    cursor.execute(sql, (f"{term}",))
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows


def get_distinct_units():
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT DISTINCT unit FROM soldiers;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows


def get_missing_rank():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM soldiers WHERE mrank IS NULL"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows

def get_by_unit(unit):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM soldiers WHERE unit = %s ORDER BY name ASC"
    cursor.execute(sql, (unit,))
    rows = cursor.fetchall()
    conn.close()
    cursor.close()
    return rows






if __name__ == "__main__":
    for row in get_by_unit("9900"):
        print(row)
