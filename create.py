from application import db
from application.models import Questions

db.drop_all()
db.create_all()

