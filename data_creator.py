
import sqlite3

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_first(conn, project):
   
   sql = '''INSERT INTO first(drugi, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, project)
   conn.commit()
   return cur.lastrowid

def add_second(conn, task):
   sql = '''INSERT INTO second(zabrane_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   project = ("test", "2020-05-11 00:00:00", "2020-05-13 00:00:00")

   conn = create_connection("testowa_baza.db")
   pr_id = add_first(conn, project)

   task = (
       pr_id,
       "test2",
       "opis2",
       "started",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )

   task_id = add_second(conn, task)

   print(pr_id, task_id)
   conn.commit()