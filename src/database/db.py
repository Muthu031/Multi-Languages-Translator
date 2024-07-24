import mariadb
import os
from dotenv import load_dotenv

load_dotenv()

class MariaDBConnection:
    def __init__(self):
        self.config = {
            'user': os.getenv('DB_USERNAME'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': int(os.getenv('DB_PORT', 3306)),  # Default to 3306 if not set
            'database': os.getenv('DB_NAME')
        }
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = mariadb.connect(**self.config)
            self.cur = self.conn.cursor()
            print("Connection established")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            self.conn = None

    def execute_query(self, query, params=None):
        if self.conn:
            try:
                self.cur.execute(query, params)
                return self.cur.fetchall()
            except mariadb.Error as e:
                print(f"Error executing query: {e}")
        else:
            print("No active database connection")
    def execute_update(self, query, params=None):
        if self.conn:
            try:
                self.cur.execute(query, params)
                self.conn.commit()
            # return self.cur.rowcount
            except mariadb.Error as e:
                print(f"Error executing query: {e}")
                self.conn.rollback()
        else:
            print("No connection to the database.")
          

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")
