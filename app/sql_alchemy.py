import datetime
from flask import Flask, current_app as app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime, Text

from app.init_app import init_app

app = init_app()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:as2d2p@127.0.0.1/parkingDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))
    mobile_no = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(512))
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    db.create_all()
    print "succcess"
