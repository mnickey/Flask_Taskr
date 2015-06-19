# Flask_Taskr/test_users.py


import os
import unittest

from views import app, db
from _config import basedir
from models import User

TEST_DB = 'test.db'

class TasksTests(unittest.TestCase):

    ############################
    #    setup and teardown    #
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()


    ########################
    #    helper methods    #
    ########################

    def login(self, name, password):
        return self.app.post('/', data=dict(
            name=name, password=password), follow_redirects=True)

    def register(self, name, email, password, confirm):
        return self.app.post(
            'register/',
            data=dict(name=name, email=email, password=password, confirm=confirm),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get('logout/', follow_redirects=True)

    def create_user(self, name, email, password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('add/', data=dict(
            name='Go to the bank',
            due_date='02/05/2015',
            priority='1',
            posted_date='02/04/2015',
            status='1'), follow_redirects=True)

    def create_admin_user(self):
        new_user = User(name='Superman', email='admin@mnickey.com', password='allpowerful', role='admin')
        db.session.add(new_user)
        db.session.commit()

    def test_admin_users_can_complete_tasks_that_are_not_created_by_them(self):
        self.create_user('Michael', 'example@yahoo.com', 'python')
        self.login('Michael', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Superman', 'allpowerful')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get("complete/1/", follow_redirects=True)
        self.assertNotIn('You can only update tasks that belong to you.', response.data)

    def test_admin_users_can_delete_tasks_that_are_not_created_by_them(self):
        self.create_user('Michael', 'example@yahoo.com', 'python')
        self.login('Michael', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Superman', 'allpowerful')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get("delete/1/", follow_redirects=True)
        self.assertNotIn('You can only delete tasks that belong to you.', response.data)
