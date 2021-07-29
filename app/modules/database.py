import psycopg2
from psycopg2.extras import Json, DictCursor
import uuid
from datetime import date


class Database:
    def __init__(self, database):
        print("[+] Connecting to database...")
        try:
            self.connection = psycopg2.connect(user=database["user"],
                                               password=database["password"],
                                               host=database["host"],
                                               port=database["port"],
                                               database=database["database"])

            self.cursor = self.connection.cursor(cursor_factory=DictCursor)
            # Print PostgreSQL Connection properties
            print(self.connection.get_dsn_parameters(), "\n")

            # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("[+] Connecting succeed to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def fetch(self, sql_query, values=()):
        self.cursor.execute(sql_query, values)
        record = self.cursor.fetchone()
        print(record)

    def execute(self, sql_query, values=()):
        self.cursor.execute(sql_query, values)
        self.connection.commit()

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("[+] PostgreSQL connection is closed")

    def store_data(self, obj, target=None):
        timestamp = date.today()
        new_id = str(uuid.uuid4())
        self.execute("""  INSERT INTO companies (id, dict, target, timestamp) VALUES (%s, %s, %s, %s) """,
                     [new_id, Json(obj), target, timestamp])
        print(f"[+] object stored!")
