from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages


# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods=['GET','POST'])
def home():
	'''
	Home page

	Display the homepage of a chat app, where you can enter an author and a message.
	The page will reload when you press Send, and display the updated dialogue.

	'''
	form = MessageForm()
	if form.validate_on_submit():
		author = User.query.filter_by(author=form.author.data).first()
        # check if user exits in database
	# if not create user and add to database
	# create row in Message table with user (created/found) add to the database
		if author is None :
			print('User not in data base')
			# add a new User into the database
			db.session.add(User(author=form.author.data))
			db.session.commit()
			# add a new message to the database which connected by the user's id
			db.session.add(Messages(message=form.message.data, user_id = User.query.filter_by(author=form.author.data).first().id))
			db.session.commit()
			print('added new user')
		# if the user already exist in the data base, create a new message and connected with the user's id
		else:
			db.session.add(Messages(message=form.message.data, user_id = User.query.filter_by(author=form.author.data).first().id))
			db.session.commit()
			print('added message')

	# create a new posts dictionary
	posts = []
	# for every message in the Messages collection, create a new dictionary with the author and message
	# then appended it to the posts dictionary.
	for m in Messages.query:
		new_m = {}
		new_m['author'] = m.author
		new_m['message'] = m.message
		posts.append(new_m)


    # output all messages
    # create a list of dictionaries with the following structure
	#posts =  [{'author':'carlos', 'message':'Yo! Where you at?!'}, {'author':'Jerry', 'message':'Home. You?'}]


	return render_template('home.html', posts=posts, form=form)


