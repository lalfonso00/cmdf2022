from flask import Flask, render_template,  request, escape
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import csv
import json
import datetime


app = Flask(__name__)

app.secret_key = 'b433ee1f1e7ea49f870e65ae6fb90ef0'
app.config["JWT_SECRET_KEY"] = 'b433ee1f1e7ea49f870e65ae6fb90ef0'

jwt = JWTManager(app)

databaseName1 = 'mongodb://newlalfonso:blandpass@cluster0-shard-00-00.rmzow.mongodb.net:27017,cluster0-shard-00-01.rmzow.mongodb.net:27017,cluster0-shard-00-02.rmzow.mongodb.net:27017/myFirstDatabase1?ssl=true&replicaSet=atlas-gpjxk4-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo1 = PyMongo(app, uri=databaseName1)
users = mongo1.db.users3
# retailers = mongo1.db.company
# loggedin = mongo1.db.loggedin


@app.route('/')
def init():                            # this is a comment. You can create your own function name
    return render_template('test.html')


@app.route('/register', methods=['POST'])
def register():

    if request.is_json:
        email = request.json['email']
        password = request.json['password']
        firstname = request.json['firstname']
        lastname = request.json['lastname']
    else:
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

    # email = request.form.get('email')
    # username = request.form.get('username')

    if users.find_one({"email": email}):
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409
        return jsonify(message='That email already exists.'), 409

    # if users.find_one({"username" : username}):
    #     return jsonify(message='That username already exists, try another'), 409   # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409
    else:
        x = {}
        x["firstname"] = firstname
        x["lastname"] = lastname
        # same as request.form.get('password')
        x["password"] = generate_password_hash(password, method='sha256')
        x["email"] = email

        print(x)
        # users.insert_one(x)

        return jsonify(message='User created successfully.'), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
