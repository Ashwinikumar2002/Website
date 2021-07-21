# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from decouple import config
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import uuid 

  
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
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (email, password, ))
		account = cursor.fetchone()
		
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['email'] = account['email']
			msg = 'Logged in successfully !'
			return render_template('login.html', msg = msg) 
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('index.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	msg = 'Logged Out successfully'
	return render_template('login.html', msg = msg)



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
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE uniqueid = % s', (uniqueid, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s)', (username, password, email, confirmemail, uniqueid ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'

	
			return redirect('http://localhost:5001/verify/'+ email +'') 
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('signup.html', msg = msg)



@app.route('/templates', methods =['GET'])
def templates():
	msg= 'Redirecting to login page'
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
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = % s', (uniqueid, ))
		elite = cursor.fetchone()
		if elite:
			msg = 'Account already exists !'
		
		else:
			cursor.execute('INSERT INTO elite VALUES (NULL, % s, % s, % s, % s)', (education, collegename, branch, uniqueid, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !' 	 
	    
			return render_template('signup.html', msg = msg, uniqueid=uniqueid, ) 
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('index.html', msg = msg)



if __name__ == "__main__":

    app.run(host="localhost", port=5003, debug=True)