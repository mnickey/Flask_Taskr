# db_migrate.py

from views import db
from _config import DATABASE_PATH
import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:
    # get cursor object to execute SQL commands
    c = connection.cursor()

    # temporarily change the name of the tasks table
    c.execute("""ALTER TABLE tasks RENAME TO old_tasks""")

    # recreate a new tasks table wuth update schema
    db.create_all()

    # retrieve data from old tasks table
    c.execute("""SELECT name, due_date, priority, status from old_tasks ORDER BY task_id ASC""")

    # save all the rows as a list of tuples; set posted date to now and user_id to 1
    data = [(row[0], row[1], row[2], row[3], datetime.now(), 1) for row in c.fetchall()]

    # insert data into tasks table
    c.executemany("""INSERT INTO tasks (name, due_date, priority, status, posted_date, user_id) Values (?, ?, ?, ?, ?, ?)""", data)

    # delete old_tasks table
    c.execute("""DROP TABLE old_tasks""")