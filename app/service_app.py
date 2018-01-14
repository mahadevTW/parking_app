from flask import Flask
from flask import request
from  flask import jsonify
from app.init_app import init_app
from app.sql_alchemy import db, User
from flask_sqlalchemy import SQLAlchemy


app = init_app()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:as2d2p@127.0.0.1/parkingDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
session_db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Welcome!"


@app.route("/api/hello")
def hi():
    return "Hello word"


@app.route("/api/login", methods=['GET', 'POST'])
def login():
    request_data = request.args
    print request_data
    username = request_data['username']
    password = request_data['password']

    user_object = User.query.filter_by(username=username)
    if user_object and user_object[0].password == password:
        return jsonify({"success": True, "responseData": [], "errorCode": 200})
    else:
        return jsonify({"success": False, "responseData": [], "errorCode": 404})


@app.route("/api/usersignup", methods=['GET', 'POST'])
def signup():
    if request.method=="GET":
        request_data = request.args
    else:
        request_data = request.get_json()
    print request_data
    db = session_db
    try:
        user_object = User(username=request_data['username'],
                           password=request_data['password'],
                           mobile_no=request_data['mobileNo'],
                           address=request_data['address'])
        db.session.add(user_object)
        db.session.commit()
        return jsonify({"success": True,
                        "responseData": {"username": user_object.username,
                                         "mobileNo": user_object.mobile_no,
                                         "address": user_object.address},
                        "errorCode": 200})
    except Exception as e:
        print e
        return jsonify({"success": False, "responseData": [], "errorCode": 404})


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=2004)
