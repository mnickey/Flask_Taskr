# db_migrate.py

from views import db
from _config import DATABASE_PATH
import sqlite3
# from datetime import datetime

# with sqlite3.connect(DATABASE_PATH) as connection:
#     # get cursor object to execute SQL commands
#     c = connection.cursor()
#
#     # temporarily change the name of the tasks table
#     c.execute("""ALTER TABLE tasks RENAME TO old_tasks""")
#
#     # recreate a new tasks table wuth update schema
#     db.create_all()
#
#     # retrieve data from old tasks table
#     c.execute("""SELECT name, due_date, priority, status from old_tasks ORDER BY task_id ASC""")
#
#     # save all the rows as a list of tuples; set posted date to now and user_id to 1
#     data = [(row[0], row[1], row[2], row[3], datetime.now(), 1) for row in c.fetchall()]
#
#     # insert data into tasks table
#     c.executemany("""INSERT INTO tasks (name, due_date, priority, status, posted_date, user_id) Values (?, ?, ?, ?, ?, ?)""", data)
#
#     # delete old_tasks table
#     c.execute("""DROP TABLE old_tasks""")

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor() # get a cursor object used to execute SQL commands
    c.execute("""ALTER TABLE users RENAME TO old_users""") # temporarily change the name of users table
    db.create_all() # recreate a new users table with updated schema
    # retrieve data from old_users table
    c.execute("""SELECT name, email, password FROM old_users ORDER BY id ASC""")
    # save all rows as a list of tuples; set role to 'user'
    data = [(row[0], row[1], row[2], 'user') for row in c.fetchall()]
    # insert data to users table
    c.executemany("""INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)""", data)
    c.execute("DROP TABLE old_users") # delete old_users table