from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  site_password = StringField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
  name = StringField('Name')
  submit = SubmitField('Search')

class RSVPForm(FlaskForm):
  rsvp_wedding = BooleanField('Are you able to come to the wedding?', validators=[DataRequired()])
  covid_ack = BooleanField('Do you agree to the COVID-19 policy?', validators=[DataRequired()])
  meal = StringField('What meal do you want?', validators=[DataRequired()])
  dietary_restrictions = StringField('Do you have any dietary restrictions?')
  address_correct = BooleanField("Is this your correct address?")
  cell = StringField('Cell-phone number')
  address = StringField('Street')
  unit = StringField('Unit')
  city = StringField('City')
  state = StringField('State')
  zip = StringField('Zip')
  general_note = StringField('Anything else you want to tell us?')
  submit = SubmitField('RSVP')

class RehearsalRSVPForm(RSVPForm):
  rsvp_rehearsal = BooleanField('Are you able to come to the rehearsal dinner?')
