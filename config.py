import yaml
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with open("config.yml") as file:
    parameters = yaml.load(file, Loader=yaml.FullLoader)
    db_user = parameters["db_user"]
    db_password = parameters["db_password"]
    db_host = parameters["db_host"]
    db_name = parameters["db_name"]
    app_port = parameters["app_port"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', db_user),
    os.getenv('DB_PASSWORD', db_password),
    os.getenv('DB_HOST', db_host),
    os.getenv('DB_NAME', db_name)
)
db = SQLAlchemy(app)

# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()
