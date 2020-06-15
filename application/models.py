from application import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(300), nullable=False)
        
    def __repr__(self):
        return ''.join([
            'Question: ', self.question, '\r\n',
            'Answer: ', self.answer, '\r\n',
            'ID: ', str(self.id), '\r\n'
            ])

#Many-to-Many Relationships¶
#If you want to use many-to-many relationships you will need to define a helper table that is used for the relationship. For this helper table it is strongly recommended to not use a model but an actual table

quiz_questions=db.Table('quiz_questions',
        db.Column('question_id', db.Integer, db.ForeignKey('questions.id'), primary_key=True),
        db.Column('quiz_id', db.Integer, db.ForeignKey('quizzes.id'), primary_key=True)
        )

class Quizzes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False, unique=True)
    questions=db.relationship('Questions', secondary=quiz_questions, lazy='subquery',
            backref=db.backref('pages', lazy=True)) 
    date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return ''.join([
            'ID: ', str(self.id), '\r\n',
            'Title: ', self.title, '\r\n',
            ])



