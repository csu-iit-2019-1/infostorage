from app import db

class UserData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	returnUrl = db.Column(db.String(240))
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	phone = db.Column(db.String(11), index=True, unique=True)

	def __repr__(self):
		return '<UserData {}>'.format(self.username)