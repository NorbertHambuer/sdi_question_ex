from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://mjmhyauqsdypod:57b9341924f89ffa5a0a658714d448dd192d8fadaf7150caace887bab75ad9d4@ec2-79-125-126-205.eu-west-1.compute.amazonaws.com:5432/dk01ml16p5qig'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:ad@localhost:5432/chatbot-generator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

@app.route('/')
def hello_world():
    return render_template("main.html")


if __name__ == '__main__':
    # app.run()
    manager.run()
