# Store this code in 'app.py' file

from preferences import create_user_preferences, read_user_preferences
from queries import READ_USER_PREFERENCES
from messages import ACCOUNTEXIST, INVALIDEMAIL, INVALIDUSERNAME, REDIRECTTOEXPERIENCEPAGE, REDIRECTTOLOGINPAGE, SUCCESSFULLLOGOUT, SUCCESSFULLREGISTER
from messages import SUCCESSFULLOGIN
from messages import FILLFORM
from queries import LOGIN_USER
from user import create_user
from flask import Flask, render_template, request, redirect, url_for, session, flash
from decouple import config
from flask_mysqldb import MySQL
import MySQLdb.cursors
from queries import *
from elite import *
from messages import *
from experience import *
from connect import *
import re
import uuid 
from user import *
  
# Printing random id using uuid1() 
print ("The random id using uuid1() is : ",end="") 
print (uuid.uuid1()) 
id=uuid.uuid1()

app = Flask(__name__)


app.secret_key = 'ashwinikumar'

app.config['MYSQL_HOST'] = config('MYSQL_HOST')
app.config['MYSQL_USER'] = config('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = config('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = config('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = config('MYSQL_CURSORCLASS')

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	print('email' in request.form)
	print('password' in request.form)
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		
		email = request.form['email']
		print(email)
		password = request.form['password']
		print(password)
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute(LOGIN_USER, (email, password, ))
		account = cursor.fetchone()
		
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['email'] = account['email']
			msg = SUCCESSFULLOGIN
			return render_template('login.html', msg = msg) 
	elif request.method == 'POST':
		msg = FILLFORM
	return render_template('index.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	msg = SUCCESSFULLLOGOUT
	return render_template('login.html', msg = msg)

def validate(account,msg,username,password,email,confirmemail,uniqueid):
    if account:
        msg = ACCOUNTEXIST
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = INVALIDEMAIL
    elif not re.match(r'[A-Za-z0-9]+', username):
        msg = INVALIDUSERNAME
    elif not username or not password or not email:
        msg = FILLFORM
    else:
			#cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s)', (username, password, email, confirmemail, uniqueid ))
			#mysql.connection.commit()
			#msg = 'You have successfully registered !'
        create_user(username,password,email,confirmemail,uniqueid)
        
def validate_elite(elite,education,msg,collegename, branch, uniqueid):
    if elite:
        msg =  ACCOUNTEXIST
    else:
        	create_user_elite(education, collegename, branch, uniqueid)
			#cursor.execute('INSERT INTO elite VALUES (NULL, % s, % s, % s, % s)', (education, collegename, branch, uniqueid, ))
			#mysql.connection.commit()
			#msg = 'You have successfully registered !' 

def validate_preferences(preferences,type, stage, companyname, companynotapply, uniqueid):
    if preferences:
        msg = ACCOUNTEXIST
    #else:
      	#create_user_preferences(type, stage, companyname, companynotapply, uniqueid)
			#cursor.execute('INSERT INTO preferences VALUES (NULL, % s, % s, % s, % s, % s)', ( type, stage, companyname, companynotapply, uniqueid ))
			#mysql.connection.commit()
			#msg = SUCCESSFULLREGISTER
def validate_experience(experience):
	if experience:
		msg= ACCOUNTEXIST

def validate_connect(connect):
	if connect:
		msg= ACCOUNTEXIST

@app.route('/register', methods =['GET', 'POST'])
def register(uniqueid=id):
	msg = ''
	print('fullname' in request.form)
	print('password' in request.form)
	print('email' in request.form)
	print('confirmemail' in request.form)
	print(uniqueid)
 
	if request.method == 'POST' and 'fullname' in request.form and 'password' in request.form and 'email' in request.form and 'confirmemail' in request.form:
		username = request.form['fullname']
		print(username)
		password = request.form['password']
		print(password)
		email = request.form['email']
		print(email)
		confirmemail = request.form['confirmemail']
		print(confirmemail)
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		#cursor.execute('SELECT * FROM accounts WHERE uniqueid = % s', (uniqueid, ))
        
		#account = cursor.fetchone()
		account = read_user(uniqueid)
		validate(account,msg,username,password,email,confirmemail,uniqueid)
		#if account:
		#	msg = 'Account already exists !'
		#elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		#	msg = 'Invalid email address !'
		#elif not re.match(r'[A-Za-z0-9]+', username):
		#	msg = 'Username must contain only characters and numbers !'
		#elif not username or not password or not email:
		#	msg = 'Please fill out the form !'
		#else:
			#cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s)', (username, password, email, confirmemail, uniqueid ))
			#mysql.connection.commit()
			#msg = 'You have successfully registered !'
        #		create_user(username,password,email,confirmemail,uniqueid)
		return redirect('http://localhost:5001/verify/'+ email +'') 
	elif request.method == 'POST':
		msg = FILLFORM
	return render_template('signup.html', msg = msg)



@app.route('/templates', methods =['GET'])
def templates():
	msg= REDIRECTTOLOGINPAGE
	return render_template('login.html', msg=msg)



@app.route('/elite', methods =['GET', 'POST'])
def elite():
	msg = ''
	print('education' in request.form)
	print('collegename' in request.form)
	print('branch' in request.form)
	print(id)
 
	if request.method == 'POST' and 'education' in request.form and 'collegename' in request.form and 'branch' in request.form :
		education = request.form['education']
		print(education)
		collegename = request.form['collegename']
		print(collegename)
		branch = request.form['branch']
		print(branch)
		uniqueid = id
		print(uniqueid)
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		#cursor.execute('SELECT * FROM accounts WHERE id = % s', (uniqueid, ))
		elite = read_user_elite(uniqueid)
		validate_elite(elite, education, msg, collegename, branch, uniqueid)
  		
		#if elite:
		#	msg = 'Account already exists !'
		
		#else:
			#cursor.execute('INSERT INTO elite VALUES (NULL, % s, % s, % s, % s)', (education, collegename, branch, uniqueid, ))
			#mysql.connection.commit()
			#msg = 'You have successfully registered !' 	 
	        #		create_user_elite(education, collegename, branch, uniqueid)
		flash("Check your email for the verification link-")
		return render_template('signup.html', msg = msg, uniqueid=uniqueid, ) 
	elif request.method == 'POST':
		msg = FILLFORM
	return render_template('index.html', msg = msg)



@app.route('/preferences', methods =['GET', 'POST'])
def preferences(uniqueid=id):
	msg = ''
	print('type' in request.form)
	print('stage' in request.form)
	print('companyname' in request.form)
	print('companynotapply' in request.form)
	print('active_passive')
 
	if request.method == 'POST' and 'type' in request.form and 'stage' in request.form and 'companyname' in request.form and 'companynotapply' in request.form:
		type = request.form['type']
		print(type)
		stage = request.form['stage']
		print(stage)
		companyname = request.form['companyname']
		print(companyname)
		companynotapply = request.form['companynotapply']
		print(companynotapply)
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		#cursor.execute(READ_USER_PREFERENCES, (uniqueid, ))
		preferences = read_user_preferences(uniqueid)
		validate_preferences(preferences,type, stage, companyname, companynotapply, uniqueid)
		#if preferences:
		#	msg = ACCOUNTEXIST
		
		#else:
		#	cursor.execute('INSERT INTO preferences VALUES (NULL, % s, % s, % s, % s, % s)', ( type, stage, companyname, companynotapply, uniqueid ))
		#	mysql.connection.commit()
		#	msg = SUCCESSFULLREGISTER
		create_user_preferences(type, stage, companyname, companynotapply, uniqueid)

		return render_template('experience.html',msg=msg) 
	elif request.method == 'POST':
		msg = FILLFORM
	return render_template('company1.html', msg = msg)

@app.route('/experience', methods=['GET','POST'])
def experience(uniqueid=id):
    msg=''
    print('years' in request.form)
    print('expertise' in request.form)
    if request.method == 'POST' and 'years' in request.form and 'expertise' in request.form:
        years = request.form['years']
        print(years)
        expertise = request.form['expertise']
        print(expertise)
        experience = read_user_experience(uniqueid)
        validate_experience(experience)
        create_user_experience(years,expertise,uniqueid)
        return render_template('connect.html',msg=msg)
    elif request.nethod == 'POST':
        msg= FILLFORM
    return render_template('experience.html',msg=msg)

@app.route('/connect', methods=['GET','POST'])
def connect(uniqueid=id):
    msg=''
    print('linkedin' in request.form)
    print('github' in request.form)
    if request.method == 'POST' and 'linkedin' in request.form and 'github' in request.form:
        linkedin = request.form['linkedin']
        print(linkedin)
        github = request.form['github']
        print(github)
        connect = read_user_connect(uniqueid)
        validate_connect(connect)
        create_user_connect(linkedin,github,uniqueid)
        return render_template('choose.html',msg=msg)
    elif request.nethod == 'POST':
        msg= FILLFORM
    return render_template('connecr.html',msg=msg)

@app.route('/next', methods =['GET'])
def next():
	msg= REDIRECTTOEXPERIENCEPAGE
	return render_template('experience.html', msg=msg)

    
    
    
if __name__ == "__main__":

    app.run(host="localhost", port=5003, debug=True)
