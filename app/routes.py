from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

#initialize database
db.create_all()

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods=['GET','POST'])
def home():

	form = MessageForm()
	if form.validate_on_submit():
		author = User.query.filter_by(author=form.author.data).first()
        # check if user exits in database
		if author is None :
			print('User not in data base')
			db.session.add(User(author=form.author.data))
			db.session.commit()
			db.session.add(Messages(message=form.message.data, user_id = User.query.filter_by(author=form.author.data).first().id))
			db.session.commit()
			print('added user')
		else:
			db.session.add(Messages(message=form.message.data, user_id = User.query.filter_by(author=form.author.data).first().id))
			db.session.commit()
			print('added message')
        # if not create user and add to database
        # create row in Message table with user (created/found) add to ta database
	
	posts = []
	for m in Messages.query:
		test_m = {}
		test_m['author'] = m.author
		test_m['message'] = m.message
		posts.append(test_m)


    # output all messages
    # create a list of dictionaries with the following structure
#	posts =  [{'author':'carlos', 'message':'Yo! Where you at?!'}, {'author':'Jerry', 'message':'Home. You?'}]

	return render_template('home.html', posts=posts, form=form)


#def messagePost():

