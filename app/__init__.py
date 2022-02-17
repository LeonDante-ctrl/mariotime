from flask import Flask



# App initialization
app = Flask(__name__)

app.config['SECRET_KEY']='mariotimeshaviya'


from app import views