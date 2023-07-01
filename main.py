from connection import create_connection, create_connection_in_memory
from data_creator import add_task, add_project
import sqlite3

if __name__ == '__main__':
   create_connection(r"testowa_baza.db")
   create_connection_in_memory()

   project = ("test", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
   conn = create_connection("database.db")
   add_project(conn, project)
   

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
