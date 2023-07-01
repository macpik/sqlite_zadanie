
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_first_sql = """
   -- first table
   CREATE TABLE IF NOT EXISTS first (
      id integer PRIMARY KEY,
      drugi parametr text NOT NULL,
      start_date text,
      end_date text
   );
   """

   create_second_sql = """
   -- second table
   CREATE TABLE IF NOT EXISTS second (
      id integer PRIMARY KEY,
      zabrane_id integer NOT NULL,
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (zabrane_id) REFERENCES first (id)
   );
   """

   db_file = "testowa_baza.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_first_sql)
       execute_sql(conn, create_second_sql)
       conn.close()