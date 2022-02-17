from flask import redirect, render_template, url_for, flash
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User



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

    user = User.query.filter_by(username=form.username.data).first()

    if user and form.password.data == user.password :

    #causing errors due to lack of the inputted username form data
    # if form.username.data == user.username and form.password.data == user.password :

    # if form.username.data == 'shaviya' and form.password.data == '123456' :
    

      flash(f'Logged in successfully for { form.username.data }', category='success text-center')

      return redirect(url_for('index'))

    else :

      flash(f'Login unsuccessful!', category='danger text-center')

  return render_template('login.html', title = title, form = form)



@app.route('/signup', methods=['post', 'get'])
def Register() :
  '''
  View registration page function that returns the registration page and its data
  '''

  title = 'Register'
  form = RegistrationForm()

  if form.validate_on_submit() :

    user = User(username=form.username.data, email=form.email.data, password=form.password.data)

    db.session.add(user)
    db.session.commit()

    flash(f'Account created successfully for { form.username.data }', category='success text-center')

    return redirect(url_for('login'))

  return render_template('signup.html', title = title, form = form)