from flask import render_template
from app import app



# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  return render_template('index.html')



@app.route('/login')
def login() :
  '''
  View login page function that returns the login page and its data
  '''

  title = 'Login'

  return render_template('login.html', title = title)