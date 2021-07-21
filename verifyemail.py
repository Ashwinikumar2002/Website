from flask import Flask,flash,render_template,request,redirect,url_for
from flask_mail import Mail,Message
from decouple import config
from flask_mysqldb import MySQL
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import MySQLdb.cursors
import re
import os
from dotenv import load_dotenv
load_dotenv()
from random import randint 
 
 
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  
mail = Mail(app)  
app.config["MAIL_SERVER"]= config('MAIL_SERVER') 
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'ashwinikumarnit19@gmail.com'  
app.config['MAIL_PASSWORD'] = 'Ashwinikumar2000'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)  

s = URLSafeTimedSerializer('Thisisasecret!')

app.config['MYSQL_HOST'] = config('MYSQL_HOST')
app.config['MYSQL_USER'] = config('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = config('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = config('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = config('MYSQL_CURSORCLASS')

mysql = MySQL(app)
otp = randint(00000000,99999999) 


@app.route('/')  
#def index():  
 #return render_template("homepage.html")  

@app.route('/verify/<email>',methods =['GET', 'POST'])  
def verify(email):  

 #email = request.form["email"]
  token = s.dumps(email, salt='email-confirm')  
  msg = Message('Hi welcome to justhire.com, Complete your sign up verification using this verification link below-',sender = 'ashwinikumarnit19@gmail.com', recipients = [email])
  link = url_for('validate', token=token, _external=True) 
  msg.body = 'Your link is {}'.format(link)   
  mail.send(msg)  
  return '<h1>The email you entered is {}. The token is {}</h1>'.format(email, token) 

@app.route('/validate/<token>')   
def validate(token):  
 try:
  email = s.loads(token, salt='email-confirm', max_age=3600)
 except SignatureExpired: 
      return '<h1>The token is expired!</h1>'
 return redirect(os.getenv('PORT_ONE'), code=302)  
 
 
if __name__ == '__main__':  
 
  app.run(host="localhost", port=5001, debug=True)