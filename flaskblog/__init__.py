from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#SECRET_KEY helps us protect from cross site forgery, modifying keys etc
#the hash value was genereated  using a 'secrets' library in python terminal
# import secrets
# secrets.token_hex(16)   #here 16 means the byte
app.config['SECRET_KEY'] = 'PUT_YOUR_SECRET_KEY_HERE'

#this is our database. It resides in our config file. ///is for relative path from the current file
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db' 

#create the databse instance
db = SQLAlchemy(app)

#this helps us to save user passwords cryptically
bcrypt = Bcrypt(app)
#this helps in login session
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes



