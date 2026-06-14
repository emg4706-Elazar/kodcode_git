import mysql.connector

def get_connection():
    return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="secret",
            database="soldiers_db"
        )


def get_summary():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
     "SELECT COUNT(*) AS total FROM soldiers;"
    )
    total = cursor.fetchone()
    cursor.execute(
        "SELECT COUNT(*) AS active FROM soldiers "
        "WHERE active = TRUE;"
    )
    active = cursor.fetchone()
    cursor.close()
    conn.close()
    inactive = {"inactive": total["total"] - active["active"]}
    summary = dict(total)
    summary.update(active)
    summary.update(inactive)

    return summary


def count_by_unit():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT unit ,COUNT(*) FROM soldiers"
    )
    [{"unit": "8200", "total": 4}, ...]
    pass

def get_missing_data():
    # Soldiers where rank IS NULL
    pass

def get_units_with_multiple_soldiers():
    # Only units that have more than 1 soldier (use
    # HAVING)
    pass





if __name__ == "__main__":
    print(get_summary())

