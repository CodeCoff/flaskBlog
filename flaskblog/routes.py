from flask  import render_template, flash, redirect,  url_for#we need url_for for static files
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app, db , bcrypt

posts = [
    {
        'author' : 'Vuwan',
        'title'  :  'Blog Post1',
        'content':  'First post content',
        'date_posted' : 'June 07, 2019'
    },
    {
        'author' : 'Mannu',
        'title'  :  'Blog Post2',
        'content':  'Second post content',
        'date_posted' : 'June 10, 2019'
    }
]

#both of the below routes will be handled by the same function
@app.route("/") 
@app.route("/home") 
def home():
    return render_template('home.html', posts = posts) #this simply means, we will have access to posts variable in template

#this means if running this script directly with python then the name will be main but if we import this modulde somewhere else,
#then the name will be the name of the module
@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


#this route handle the registration page for the new user.

@app.route("/register", methods=['GET', 'POST'])
def register():
    #create an instance of RegistrationForm
    form = RegistrationForm()

    #this will tell us if the form is validated when submitted
    # 'success' is a bootstrap provided function
    if form.validate_on_submit():
        #hased_password stores the user created pw cryptically to the database
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #create a  new user with the entered information
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        #add the user and commit to the database
        db.session.add(user)
        db.session.commit()
        #flash the message
        flash('Your account has been created! You are now able to login', 'success')
        #redirect the user to the login page
        return redirect(url_for('login'))
        flash(f'Account created for {form.username.data}!', 'success')

        #redirect user to the 'home' page i.e. home function, after the form is validated
        return redirect(url_for('home'))
    
    #render the register.html page with "Register" title at the title bar.
    return render_template('register.html', title='Register', form= form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    #create an instance of LoginForm
    form = LoginForm()   

    #validate the login information of the user
    if form.validate_on_submit():
        if form.email.data== 'admin@blog.com' and form.password.data=='password':
            flash('You\'ve been logged in!', 'success')
            #redirect user to the 'home' page i.e. home function, after the form is validated
            return redirect(url_for('home'))
        
        #In case of user entering wrong username and pw; the following will flash the 'Login 
        #Unsuccessful method
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form= form)

@app.route("/account")
def account():
    image_file = url_for('static', filename='profile_pics/'+current_user.images_file)
    return render_template('account.html', title='Account', image_file=image_file)

