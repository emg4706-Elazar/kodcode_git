import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )

conn = get_connection()

cursor = conn.cursor()

create_new_table = """
CREATE TABLE IF NOT EXISTS soldiers (
    id  INT     PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(100) NOT NULL,
    mrank   VARCHAR(50),
    unit    VARCHAR(100),
    active  BOOLEAN DEFAULT TRUE
)
"""

cursor.execute(create_new_table)

conn.close()
cursor.close()

print("New table was created successfully")




















