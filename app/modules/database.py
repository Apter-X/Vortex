import psycopg2
import uuid


class Database:
    def __init__(self, config):
        print("[+] Connecting to database...")
        try:
            self.connection = psycopg2.connect(user=config["user"],
                                               password=config["password"],
                                               host=config["host"],
                                               port=config["port"],
                                               database=config["database"])

            self.cursor = self.connection.cursor()
            # Print PostgreSQL Connection properties
            print(self.connection.get_dsn_parameters(), "\n")

            # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("[+] Connecting succeed to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        self.ids = {}

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

    def check_table(self, table):
        self.fetch(f""" SELECT * FROM {table} """)

    def create_row(self, table, dic, uid_key=None, foreign_key=None):
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

        query = f"""  INSERT INTO {table} ({keys_str}) VALUES ({keys_pointer}) """
        # self.execute(query, values)
        print(query, values)
        return {uid_key: uid_val}
