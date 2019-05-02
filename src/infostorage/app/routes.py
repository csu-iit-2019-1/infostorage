from flask import render_template, flash, redirect, request, abort, jsonify
from app import app, db
from app.models import UserData
from app.forms import PersonalDataForm
from requests.models import PreparedRequest

import logging
from logging.handlers import RotatingFileHandler
from time import strftime

@app.route('/admin/print_all/', methods=['GET'])
def print_all():
	users = UserData.query.all()
	return jsonify([user.to_dict() for user in users]), 200

@app.route('/admin/delete_all/', methods=['GET'])
def delete_all():
	res = db.session.query(UserData).delete()
	db.session.commit()
	return jsonify(msg="OK"), 200

@app.route('/', methods=['GET'])
def get_user_data():
	siteId = request.args.get("siteId") #GET
	if siteId is not None and siteId != "":
		userData = UserData.query.filter_by(id=siteId).first_or_404()
		return jsonify(userData.to_dict()), 200
	else:
		abort(404)
	
@app.route('/enter-new-data/', methods=['GET', 'POST'])
def enter_new_data():
	error = None
	returnUrl = request.args.get("returnUrl") #GET
	if returnUrl is not None and returnUrl != "":
		form = PersonalDataForm()
		if request.method == 'POST' and form.validate():
			userData = UserData(
				returnUrl=returnUrl, 
				firstName=form.firstName.data, 
				lastName=form.lastName.data, 
				username=form.username.data, 
				email=form.email.data, 
				phone=form.phone.data
				)
			db.session.add(userData)
			db.session.commit()
			siteId = userData.id
			return redirect(add_param_to_url(returnUrl, {'siteId': str(siteId)}))
		return render_template('personal_data.html', title='Infostorage - Personal Data', form=form, error=error)
	else:
		abort(404)

@app.route('/logs/', methods=['GET'])
def get_logs():
        return render_template('app.log', title = 'Infostorage - Logs')		

@app.after_request
def after_request(response):
    handler = RotatingFileHandler('app/templates/app.log')
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.ERROR)

    if (logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(handler)
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s <br>', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

def add_param_to_url(url, params):
	req = PreparedRequest()
	req.prepare_url(url, params)
	return req.url


#u = User.query.get(2)
#db.session.delete(u)
#User.query.filter_by(id=2).delete()
