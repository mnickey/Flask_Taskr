import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    # make a cursor object
    c = connection.cursor()

    # create the tables
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  due_date TEXT NOT NULL,
                  priority INTEGER NOT NULL,
                  status INTEGER NOT NULL)""")

    # insert seed data
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish the tutorial", "06/09/2015", 10, 1)'
    )
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish Real Python Course 2", "06/09/2015", 10, 1)'
    )
