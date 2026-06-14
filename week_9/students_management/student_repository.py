from db_connection import conn

def create_student(name: str, age: int, course: str,
                   email: str | None, status: str = "active"):
    cursor = conn.cursor()
    sql = """
    INSERT INTO students (name, age, course)
    VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(sql, (name, age, course))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        conn.close()
        return f"{e}"
    finally:
        cursor.close()

print(create_student("Moshe", 30, "kodcode", "emg4706@gmail.com"))









