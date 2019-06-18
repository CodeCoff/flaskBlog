from flaskblog import db, login_manager
from datetime import datetime

'''
To run the database interface, enter python terminal within your project folder i.e. flaskblog
in our case. Do 'from flaskblog import db'
- create database         db.create_all()               (this will create site.db file)
- import models         from flaskblog.models import User, Post
- add user              db.session.add()
- commit the change     db.session.commit()
- query the database:
    -User.query.all()                                     all users
    -User.query.first()                                   first user
    -User.query.filter_by(username='Vuwan').all()         filter the users by username='Vuwan'
    - user = User.query.filter_by(username='Vuwan').all() assigns the filtered result to the 'user' variable
       
'''
#this is a database table representing User and is extending 
# db.Model. It represents the user profile of the blog
#to open db: 1) open python cli 2) from flaskblog import db 3) db.create_all() 4) db.session.commit() #to commit the changes
#to query : User.query.all() : To filter the user by username- User.query.filter_by(username='Corey'.all())
class User(db.Model):
    #these are the columns of the database table
    ##column 1
    id = db.Column(db.Integer, primary_key=True) 
    #column 2, and is unique. It can't be null
    username = db.Column(db.String(20), unique=True,  nullable=False) 
    #column 3, and is unique. It can't be null
    email = db.Column(db.String(120), unique=True,  nullable=False) 
    #column 4. It has a default image i.e. default.jpg
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') 
    # column 5. These will be stored has hash. Not unique because people can have same password
    password = db.Column(db.String(60), nullable=False) 
    #column 6. This has a relationship to 'Post' model. lazy defines when sqlAlchemy loads
    #the data from the database. True means the data will be loaded in one go.
    posts = db.relationship('Post', backref='author', lazy=True) 

    #this dunder method(double underscore method) will return when the "User" is called
    #this is helpful when working with database interface
    def __repr__(self):
        return f"User('{self.username}', {self.email}, {self.image_file}')"

# this is a database table representing class which is
# inheriting from db.model. It represents the articles posted by the user 
class Post(db.Model):
     #these are the columns of the database table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    #this is a foreign key and has a relationship to user.id
    #we've lower case user.id because we are only referencing here. 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    def __repr__(self):
        return f"Post('{self.title}', {self.date_posted}')"


