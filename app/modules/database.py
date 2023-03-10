import uuid
import psycopg2
from psycopg2.extras import Json, DictCursor, NamedTupleCursor


class Database:
    def __init__(self, config):
        try:
            self.connection = psycopg2.connect(user=config["user"],
                                               password=config["password"],
                                               host=config["host"],
                                               port=config["port"],
                                               database=config["database"],
                                               keepalives=1,
                                               keepalives_idle=30,
                                               keepalives_interval=10,
                                               keepalives_count=5
                                               )

            self.cursor = self.connection.cursor(cursor_factory=DictCursor)
            # Print Postgresql Connection properties
            # print(self.connection.get_dsn_parameters(), "\n")

            # Print Postgresql version
            # self.cursor.execute("SELECT version();")
            # record = self.cursor.fetchone()
            # print("[+] Connecting succeed to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to Postgresql!", error)

        self.ids = {}

    def fetch(self, sql_query):
        self.cursor.execute(sql_query)
        record = self.cursor.fetchone()
        return record

    def fetch_assoc(self, sql_query):
        self.cursor = self.connection.cursor(cursor_factory=NamedTupleCursor)

        self.cursor.execute(sql_query)
        record = self.cursor.fetchone()
        return record

    def fetchone(self, table, values=()):
        self.cursor.execute("""SELECT * FROM {}""".format(table), values)
        record = self.cursor.fetchone()
        return record

    def fetchall(self, table, values=()):
        self.cursor.execute("""SELECT * FROM {}""".format(table), values)
        record = self.cursor.fetchall()
        return record

    def fetchall_assoc(self, table):
        self.cursor = self.connection.cursor(cursor_factory=NamedTupleCursor)

        self.cursor.execute("""SELECT * FROM {}""".format(table))
        record = self.cursor.fetchall()
        return record

    def execute(self, sql_query, values=(), commit=False):
        self.cursor.execute(sql_query, values)
        if commit:
            self.commit()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Postgresql connection is closed.")

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def store_brute_data(self, obj, target=None, targeted_link=None):
        # timestamp = date.today()
        # new_id = str(uuid.uuid4())
        self.execute("""INSERT INTO companies (dict, target, targeted_link) VALUES (%s, %s, %s)""",
                     [Json(obj), target, targeted_link], commit=True)

    def store_data(self, table, dic, uid_key=None, foreign_key=None):
        """Parameters
        ----------
        table : basestring
        dic : dict
        uid_key : basestring
        foreign_key : dict
        """
        uid_val = ""
        targets = list(dic.keys())
        values = list(dic.values())
        keys_str = str()
        keys_pointer = str()

        if uid_key:
            uid_val = str(uuid.uuid4())
            targets.insert(0, uid_key)
            values.insert(0, uid_val)
            self.ids[uid_key] = uid_val

        if foreign_key:
            targets.insert(1, foreign_key)
            values.insert(1, self.ids[foreign_key])

        for i, target in enumerate(targets):
            if i != len(targets) - 1:
                keys_str += target + ', '
                keys_pointer += "%s, "
            else:
                keys_str += target
                keys_pointer += "%s"

        query = f"""INSERT INTO {table} ({keys_str}) VALUES ({keys_pointer})"""

        self.execute(query, values)
        print(query, values)
        return {uid_key: uid_val}

    def refresh_mat_view(self, view_name, with_data=True):
        query = f"""REFRESH MATERIALIZED VIEW {view_name}"""
        if with_data:
            query += ";"
        else:
            query += " WITH NO DATA;"
        self.execute(query)

    def __del__(self):
        self.disconnect()
