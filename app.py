from flask import Flask
from flask import request
from  flask import jsonify
import MySQLdb
app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome!"
@app.route("/hello")
def hi():
    return "Hello word"
@app.route("/login", methods=['GET', 'POST'])
def login():
    request_data = request.args
    print request_data
    username = request_data['username']
    password = request_data['password']
    db = MySQLdb.connect("localhost","root","","demo" )
    cursor = db.cursor()
    query = "select *from user where username=%s"
    cursor.execute(query, [username])
    list_data  = list(cursor.fetchall())
    entry = list_data[0]
    if entry[0] == username and entry[1] == password:
        return jsonify({"success": True, "responseData": [], "errorCode": 200})
    else:
        return jsonify({"success": False, "responseData": [], "errorCode": 404})


@app.route("/signup", methods = ['GET', 'POST']):
def signup():
    request_data = request.

if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True,port=2004)
