from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, login_required
from .forms import LoginForm, SearchForm, RSVPForm, RehearsalRSVPForm
from .models import User, Group
from .logged_in import SessionUser
from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='Main')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    if form.site_password.data != "BK is from Texas":
      flash(f'Wrong password!')
      return redirect(url_for('login'))
    login_user(SessionUser(), remember=True)
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign in', form=form)

@app.route('/fun')
def fun():
  return render_template('fun.html', title='Fun')

@app.route('/about')
def about():
  return render_template('about.html', title='About the Wedding Party')

@app.route('/rsvp', methods=['GET', 'POST'])
@login_required
def rsvp():
  form = SearchForm()
  if form.validate_on_submit():
    # Slow but whatever
    all_names, all_ids = zip(*[(f"{u.first_name} {u.last_name}", u.uid) for u in User.query.all()])
    if form.name.data in all_names:
      idx = all_names.index(form.name.data)
      flash(f"Found {form.name.data}")
      return redirect(url_for('rsvp2', uid=all_ids[idx]))
    else:
      flash(f"Did not find {form.name.data}")
      return redirect(url_for('rsvp'))
  return render_template('rsvp.html', title='RSVP', form=form)

@app.route('/rsvp_for', methods=['GET', 'POST'])
@login_required
def rsvp2():
  form = RSVPForm()
  if request.args.get("uid"):
    uid = request.args.get("uid")
    user = User.query.get(uid)
    group = Group.query.get(user.group_id)
    if form.validate_on_submit():
      flash(f"RSVPing for {user}")
      return redirect(url_for('index'))
    return render_template('rsvp2.html', 
        title='RSVP', 
        form=form, 
        user=user, 
        group=group)
  return redirect(url_for('rsvp'))

@app.route('/faq')
def faq():
  return render_template('faq.html', title='FAQ')

@app.route('/schedule')
@login_required
def schedule():
  return render_template('schedule.html', title='Schedule')

@app.route('/location')
@login_required
def location():
  return render_template('location.html', title='Schedule')