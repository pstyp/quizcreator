import unittest

from flask import url_for, request, redirect, render_template
from flask_testing import TestCase

from application import app, db
from application.models import Questions, Quizzes
from os import getenv



class TestBase(TestCase):

    def create_app(self):
        config_name='testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app


    def setUp(self):
       # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()
        db.session.commit()


    def create_test_quiz(self):
        return self.client.post(
                url_for('quiz'),
                data=dict(
                    title='My quiz',
                    ),
                follow_redirects=True
                )
    def create_test_question(self):
        return self.client.post(
                url_for('questions'),
                data=dict(
                    question='My question',
                    answer='My answer'
                    ),
                follow_redirects=True
                )

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()



class TestViews(TestBase):

    def test_homepage_view(self):
        response=self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response=self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_quiz(self):
        response=self.client.get(url_for('quiz'))
        self.assertEqual(response.status_code, 200)
    def test_questions(self):
        response=self.client.get(url_for('questions'))
        self.assertEqual(response.status_code, 200)


class TestPosts(TestBase):
    def test_add_quiz(self):
        with self.client:
            response=self.create_test_quiz()
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'My quiz', response.data)
        with self.client:
            response=self.client.get(url_for('quiz'))
            self.assertEqual(response.status_code, 200)
  
    def test_update_quiz(self):
        self.create_test_quiz()
        response=self.client.post(
                'update_quiz/1',
                data=dict(
                    title='New name',
                    ),
                follow_redirects=True
                )
        self.assertIn(b'New name', response.data)

    def test_remove_quiz(self):
        self.create_test_quiz()
        before_count=Quizzes.query.count()
        self.client.post('/delete_quiz/1',
                follow_redirects=True
                )
        after_count=Quizzes.query.count()
        assert before_count>after_count


    def test_delete_question(self):
        self.create_test_question()
        before_count=Questions.query.count()
        self.client.post('/delete_question/1',
                follow_redirects=True
                )
        after_count=Questions.query.count()
        assert before_count>after_count

    def test_update_question(self):
        self.create_test_question()
        response=self.client.post(
                'update_question/1',
                data=dict(
                    question='New question', 
                    ),
                follow_redirects=True
                )
        self.assertIn(b'New question', response.data)

    def test_question(self):
        with self.client:
            response=self.create_test_question()
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'My question', response.data)
        with self.client:
            response=self.client.get(url_for('questions'))
            self.assertEqual(response.status_code, 200)

    def test_add_question(self):
        self.create_test_question()
        self.create_test_quiz()
        response=self.client.post(
                '/quiz/add_question_to_quiz/1',
                data=dict(
                    question='My question',
                    ),
                follow_redirects=True
                )
        self.assertIn(b'My question', response.data)
