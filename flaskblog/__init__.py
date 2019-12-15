from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdqwdw1231231v1utc"

db = SQLAlchemy(app)
from flaskblog import routes
