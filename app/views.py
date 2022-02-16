from flask import redirect, render_template, url_for
from app import app
from app.forms import RegistrationForm, LoginForm



# Views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  return render_template('index.html')



@app.route('/login', methods=['post', 'get'])
def login() :
  '''
  View login page function that returns the login page and its data
  '''

  title = 'Login'
  form = LoginForm()

  if form.validate_on_submit() :

    if form.username.data == 'shaviya' and form.password.data == '123456' :
      return redirect(url_for('index'))

    else :

      return redirect(url_for('login'))

  return render_template('login.html', title = title, form = form)



@app.route('/signup', methods=['post', 'get'])
def Register() :
  '''
  View registration page function that returns the registration page and its data
  '''

  title = 'Register'
  form = RegistrationForm()

  if form.validate_on_submit() :
    return redirect(url_for('login'))

  return render_template('signup.html', title = title, form = form)