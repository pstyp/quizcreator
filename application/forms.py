from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from application.models import Questions

class QuestionForm(FlaskForm):
    question = StringField('Question: ',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    answer  = StringField('Answer: ',
        validators = [
            DataRequired(),
            Length(min=1, max=100)
        ]  
        )
    submit = SubmitField('Submit!')


class QuizForm(FlaskForm):
    title=StringField('Title',
            validators=[
                DataRequired(),
                Length(min=1, max=100)
        ]
        )
    
    submit = SubmitField('Submit!')

class AddQuestionToQuizForm(FlaskForm):
        question=SelectField("Select your questions",
            coerce=int,
            choices=[
                (question.id, question.question) for question in Questions.query.all()
                ]
            )
        add_quest=SubmitField('Add question!')
