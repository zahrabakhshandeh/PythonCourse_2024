import mysql.connector

class DB:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connect = None

    def connection(self):
        self.connect = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )

    def execute_query(self, query, data=None, fetch=False):
        try:
            self.connection()
            cursor = self.connect.cursor()
            cursor.execute(query, data)
            if fetch:
                return cursor.fetchall()
            self.connect.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.connect and self.connect.is_connected():
                cursor.close()
                self.connect.close()

    def add(self, table_name, values):
        result = ", ".join(["%s"]*len(values))
        query = f"INSERT INTO {table_name} VALUES ({result})"
        self.execute_query(query, data=values)

    def remove(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)

    def update(self, table_name, updates, condition):
        set_data = ", ".join([f"{col}=%s" for col in updates.keys()])
        query = f"UPDATE {table_name} SET {set_data} WHERE {condition}"
        data = tuple(updates.values())
        self.execute_query(query, data)

    def search(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}" + (f" WHERE {condition}" if condition else "")
        result = self.execute_query(query, fetch=True)
        return result
