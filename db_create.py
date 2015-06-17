# project/db_create.py


from views import db
from models import Task
from datetime import date

# create the database and the db table
db.create_all()

# insert data
# db.session.add(Task("Finish this tutorial", date(2015, 06, 18), 10, 1))
# db.session.add(Task("Complete Real Python Tasks", date(2015, 06, 20), 10, 1))

# commit changes
db.session.commit()
