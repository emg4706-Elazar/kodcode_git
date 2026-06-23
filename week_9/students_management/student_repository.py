from db_connection import get_connection

def create_student(name: str, age: int, course: str,
                   email: str | None, status: str = "active"):
    conn = get_connection()
    sql = """
    INSERT INTO students (name, age, course)
    VALUES (%s, %s, %s)
    """
    cursor = conn.cursor()
    try:
        cursor.execute(sql,(name, age, course))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        return f"{e}"
    finally:
        cursor.close()
        conn.close()


print(create_student("Moshe", 30, "kodcode", "emg4706@gmail.com"))









