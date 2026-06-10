import mysql.connector
from logging_config import l1



class IntelMessagesDAL:

    VALID_CLASSIFICATIONS = ('unclassified', 'confidential', 'secret', 'top_secret')

    def __init__(self, host: str, user: str, password: str, database: str,logger):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.logger = logger         # store logger object reference in self


    # ------------------------------------------------------------------ setup
    def get_conn(self):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return conn

    def setup(self)-> None:
        conn = self.get_conn()
        cursor = conn.cursor()
        creation_table = """
        CREATE TABLE IF NOT EXISTS intel_messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        unit VARCHAR(100) NOT NULL,
        classification ENUM('unclassified','confidential','secret','top_secret'),
        content TEXT NOT NULL,
        source VARCHAR(100),
        created_at DATETIME DEFAULT NOW())
        """
        column_definitions = """
        INSERT INTO intel_messages (unit, classification, content, source) VALUES
        ('8200', 'confidential',  'Suspicious movement detected near northern grid.', 'field agent'),
        ('8200', 'secret', 'Encrypted signal intercepted on frequency 312.', 'sigint'),
        ('9900', 'top_secret', 'Satellite image shows vehicle convoy at dawn.', 'satellite'),
        ('9900', 'unclassified',  'Routine patrol completed. No incidents reported.',  NULL),
        ('8200', 'secret', 'Drone feed shows activity near the eastern border.','drone feed'),
        ('Unit3','confidential',  'Local source reports increased foot traffic.', NULL);
        """
        cursor.execute(creation_table)
        cursor.execute(column_definitions)
        conn.commit()
        cursor.close()
        conn.close()
        return

# ------------------------------------------------------------------
# schema
    def get_schema(self)-> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        sql = "DESCRIBE intel_messages;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    # ------------------------------------------------------------ read (all)
    def get_all(self)-> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM intel_messages;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    # --------------------------------------------------------- read (by id)
    def get_by_id(self, message_id: int)-> dict | None:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM intel_messages WHERE id = %s;"
        cursor.execute(sql, (message_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return row
        return None

    # ----------------------------------------------------------------- create
    def create(self, unit: str, classification: str,
               content: str, source: str | None)-> int:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        sql = """
        INSERT INTO intel_messages (unit, classification, content, source)
        VALUES (%s, %s, %s, %s);
        """
        values = (unit, classification, content, source)
        cursor.execute(sql, values)
        new_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return new_id

    # ----------------------------------------------------------------- update
    def update(self, message_id: int, data: dict)-> bool:
        # Build a dynamic SET clause from the keys in data
        # Only update the columns that are present in data
        # Commit the transaction
        # Return True if a row was changed, False if the id did not exist
        # Never use f-strings for values — only %s
        ...
    # ----------------------------------------------------------------- delete
    def delete(self, message_id: int):#-> bool:
        conn = self.get_conn()
        cursor = conn.cursor()
        sql = """
        DELETE FROM intel_messages WHERE id = %s;
        """
        cursor.execute(sql, (message_id,))
        conn.commit()
        deleted = cursor.rowcount
        cursor.close()
        conn.close()
        return bool(deleted)

    # --------------------------------------------------------------- queries
    def get_by_unit(self, unit: str)-> list[dict]:
        # All messages where unit matches, ordered by created_at DESC
        ...
    def get_by_classification(self, classification: str)-> list[dict]:
        # All messages at the given classification level
        ...
    def get_by_unit_and_classification(self, unit: str, classification: str) -> list[dict]:
        # Both filters combined with AND
        ...
    def get_distinct_units(self)-> list[str]:
        # All unique unit values — return a plain list of strings, not dicts
        ...
    def search_content(self, term: str)-> list[dict]:
        # Rows where content contains term (partial match)
        ...
    def get_missing_source(self)-> list[dict]:
        # Rows where source IS NULL
        ...
    # ----------------------------------------------------------------- close
    def close(self)-> None:
        # Close the cursor and the connection
        ...

if __name__ == "__main__":
    im_dal = IntelMessagesDAL("127.0.0.1", "root",
                              "secret","soldiers_db",l1)
    for row1 in im_dal.get_all():
        print(row1)
    print(im_dal.delete(13))
    for row1 in im_dal.get_all():
        print(row1)
