from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# App initialization
app = Flask(__name__)

db = SQLAlchemy(app)



# app configurations
app.config['SECRET_KEY']='mariotimeshaviya'

# configuring the database for SQLLite
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/mario.db'

# configuring the database for postgres
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Access@localhost/mario'





from app import views