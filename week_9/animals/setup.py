import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="animals_db"
    )

conn = get_connection()
cursor = conn.cursor(dictionary=True)
sql = """
CREATE TABLE IF NOT EXISTS animals (
id  INT     AUTO_INCREMENT    PRIMARY KEY,
name    VARCHAR(50),
type_animal     VARCHAR(50),
age     INT
);
"""
cursor.execute(sql)
conn.commit()
cursor.execute("DESCRIBE animals;")
rows = cursor.fetchall()
cursor.close()
conn.close()

for row in rows:
    print(row)








