from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import UserData

class PersonalDataForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(max=64)])
	firstName = StringField('FirstName', validators=[DataRequired(), Length(max=64)])
	lastName = StringField('LastName', validators=[DataRequired(), Length(max=64)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(max=64)])
	phone = StringField('Phone', validators=[DataRequired(), Length(min=11, max=11)])
	submit = SubmitField('Отправить')

	def validate_phone(self, phone):
		try:
			int(phone.data)
		except ValueError:
			raise ValidationError('Phone should consists only numbers')