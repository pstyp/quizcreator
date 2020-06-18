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

        quiz=Quizzes(title='QuizTest')
        question=Questions(question='question1', answer='answer1')

        db.session.add(quiz)
        db.session.add(question)
        db.session.commit()
        
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





