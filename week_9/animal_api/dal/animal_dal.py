from db import get_connection

class AnimalDAL:

    def create_animal(self, name, type_animal, age):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO animals (name, type_animal, age)
        VALUES (%s, %s, %s);
        """
        values = (name, type_animal, age)
        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_animals(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM animals;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
