from app import db

class User(db.Model):
    # have the following columns
    # id (int)
	id = db.Column(db.Integer, primary_key=True)
    # author (string, unique, can't be null)
	author = db.Column(db.String, nullable=False, unique=True)
    # message (linkd to Messages table)
	message = db.relationship('Messages', backref = 'author', lazy='dynamic')


	def __repr__(self):
		return f'{self.author}'

class Messages(db.Model):
    # have the following columns
    # id (int)
	id = db.Column(db.Integer, primary_key = True)
    # message (string, not unique, can't be null)
	message = db.Column(db.String(256))
    # user_id link to id (int)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # write __repr__ that outputs
	def __repr__(self):
		return 'Messages: {}'.format(self.message)
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message