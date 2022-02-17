# import email
# from email.policy import default

# from click import password_option
from app import db
from datetime import datetime




class User(db.Model) :
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(30), default='default.jpg', nullable=False)
  password = db.Column(db.String(20), nullable=False)
  # date_created = db.Column(db.Datetime, default=datetime.utcnow)

  def __repr__(self) :
      return f'{self.username} : {self.email} '


      # {self.date_created}