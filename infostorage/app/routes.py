from flask import render_template, flash, redirect
from app import app, db
from app.models import User
from app.forms import RegisterForm


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'amaya'}
	return render_template('index.html', title='Home', user=user)
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
	  user = User(username=form.username.data, email=form.email.data)
	  db.session.add(user)
	  db.session.commit()
	  flash('You are register')
	  return redirect('http://google.com')
	return render_template('register.html', title='Register', form=form)
