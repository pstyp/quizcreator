from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('MY_DATABASE_URI'))
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.getenv('MY_SECRET_KEY')

from application import routes
