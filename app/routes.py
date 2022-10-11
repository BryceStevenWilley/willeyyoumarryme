from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='Main')

@app.route('/fun')
def fun():
  return render_template('fun.html', title='Fun')

@app.route('/about')
def about():
  return render_template('about.html', title='About the Wedding Party')

@app.route('/rsvp')
def rsvp():
  return render_template('rsvp.html', title='RSVP')

@app.route('/faq')
def faq():
  return render_template('faq.html', title='FAQ')

@app.route('/schedule')
def schedule():
  return render_template('schedule.html', title='Schedule')

@app.route('/location')
def location():
  return render_template('location.html', title='Schedule')