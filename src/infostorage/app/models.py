from app import db

class UserData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	returnUrl = db.Column(db.String(240))
	username = db.Column(db.String(64))
	firstName = db.Column(db.String(64))
	lastName = db.Column(db.String(64))
	email = db.Column(db.String(120))
	phone = db.Column(db.String(11))

	def __repr__(self):
		return '<UserData {}>'.format(self.username)
	
	def to_dict(self):
		return { 
			"id": self.id,
			"returnUrl": self.returnUrl,
			"username": self.username,
			"firstName": self.firstName,
			"lastName": self.lastName,
			"email": self.email,
			"phone": self.phone
			}