from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import UserData

class PersonalDataForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(max=64)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
	phone = StringField('Phone', validators=[DataRequired(), Length(min=11, max=11)])
	submit = SubmitField('Отправить')

	def validate_username(self, username):
		userData = UserData.query.filter_by(username=username.data).first()
		if userData is not None:
			raise ValidationError('Username already exists in infostorage')

	def validate_email(self, email):
		userData = UserData.query.filter_by(email=email.data).first()
		if userData is not None:
			raise ValidationError('Email already exists in infostorage')

	def validate_phone(self, phone):
		userData = UserData.query.filter_by(phone=phone.data).first()
		if userData is not None:
			raise ValidationError('Phone already exists in infostorage')
		try:
			int(phone.data)
		except ValueError:
			raise ValidationError('Phone should consists only numbers')