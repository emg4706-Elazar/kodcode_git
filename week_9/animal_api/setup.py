import mysql.connector


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








