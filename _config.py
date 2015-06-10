import os

# get the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
# WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
SECRET_KEY = 'super_secret_key'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# Database URI
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH