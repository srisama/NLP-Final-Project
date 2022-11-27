from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
 
 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

# class Offerings(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(150))
#     address=db.Column(db.String(150))
#     city=db.Column(db.String(20))
#     zip=db.Column(db.String(15))
#     state=db.Column(db.String(2))
#     hotel_class=db.Column(db.String(5))
#     review = db.relationship('Reviews')

# class Reviews(db.Model):
#     Ratings_overall = db.Column(db.Integer)
#     Title=db.Column(db.String(1000))
#     Review=db.Column(db.String(2000))
#     date_stayed=db.Column(db.String(150))
#     id = db.Column(db.Integer,primary_key=True)
#     offering_id = db.Column(db.Integer, db.ForeignKey('offerings.id'))

class Trip_Advisor_Reviews(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Ratings_overall = db.Column(db.Integer)
    Title=db.Column(db.String(1000))
    Review=db.Column(db.String(2000))
    date_stayed=db.Column(db.String(150))
    offering_id = db.Column(db.Integer)
    name=db.Column(db.String(150))
    hotel_class=db.Column(db.String(5))




    
    



