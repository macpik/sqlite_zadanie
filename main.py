from connection import create_connection, create_connection_in_memory
from data_creator import add_task, add_project
from data_select import select_all
from tables_creator import execute_sql
from data_update import update
from data_delete import delete_all, delete_where
import sqlite3

if __name__ == '__main__':

   create_project_sql = """
   -- project table
   CREATE TABLE IF NOT EXISTS project (
      id integer PRIMARY KEY,
      drugi parametr text NOT NULL,
      start_date text,
      end_date text
   );
   """

   create_task_sql = """
   -- task table
   CREATE TABLE IF NOT EXISTS task (
      id integer PRIMARY KEY,
      zabrane_id integer NOT NULL,
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (zabrane_id) REFERENCES project (id)
   );
   """

   db_file = "testowa_baza.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_project_sql)
       execute_sql(conn, create_task_sql)
       conn.close()

   create_connection(r"testowa_baza.db")
   project = ("test", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
   conn = create_connection("testowa_baza.db")
   add_project(conn, project)
   pr_id = add_project(conn, project)

   task = (
       pr_id,
       "test2",
       "opis2",
       "started",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )

   task_id = add_task(conn, task)

   print(pr_id, task_id)
   conn.commit()

   select_all(conn, 'project')

   conn = create_connection("testowa_baza.db")
   update(conn, "project", 2, status="ended")
   update(conn, "task", 1, start_date="never")
   conn.close()

   conn = create_connection("testowa_baza.db")
   delete_where(conn, "project", id=1)
   conn.close()