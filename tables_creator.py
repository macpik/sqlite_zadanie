
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