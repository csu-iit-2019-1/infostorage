from flask import render_template, flash, redirect, request, abort
from app import app, db
from app.models import UserData
from app.forms import PersonalDataForm
from requests.models import PreparedRequest


@app.route('/', methods=['GET', 'POST'])
def get_user_data():
	siteId = request.args.get("siteId") #GET
	if siteId is not None and siteId != "":
		userData = UserData.query.filter_by(id=siteId).first_or_404()
		data = userData.username + " | " + userData.returnUrl + " | " + userData.email + " | " + userData.phone
		return render_template('index.html', title='Infostorage - Get info by SiteId', data=data)
	else:
		abort(404)
	
@app.route('/enter-new-data', methods=['GET', 'POST'])
def enter_new_data():
	returnUrl = request.args.get("returnUrl") #GET
	if returnUrl is not None and returnUrl != "":
		form = PersonalDataForm()
		if form.validate_on_submit():
			userData = UserData(returnUrl=returnUrl, username=form.username.data, email=form.email.data, phone=form.phone.data)
			db.session.add(userData)
			db.session.commit()
			userData = UserData.query.filter_by(returnUrl=returnUrl, username=form.username.data, email=form.email.data, phone=form.phone.data).first()
			siteId = userData.id
			return redirect(add_param_to_url(returnUrl, {'siteId': str(siteId)}))
		return render_template('personal_data.html', title='Infostorage - Personal Data', form=form)
	else:
		abort(404)

def add_param_to_url(url, params):
	req = PreparedRequest()
	req.prepare_url(url, params)
	return req.url