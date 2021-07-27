from queries import DELETE_USER, READ_USER, UPDATE_USER
from queries import INSERT_INTO_DATABASE
from flask import Flask,render_template,request,redirect
from queries import *
from decouple import config
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()
import MySQLdb
import os
 
#app = Flask(__name__)
 
#app.secret_key = 'ashwinikumar'

#mysql = MySQL(app)


def create_user(username, password, email, confirmemail, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("inside create messsage")
    cursor.execute( INSERT_INTO_DATABASE, (username,password,email,confirmemail,uniqueid))
    db.commit()
    
    

def read_user(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( READ_USER , (uniqueid, ))
    account = cursor.fetchone()
    return account

    
def delete_user(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( DELETE_USER, (uniqueid, ))
    db.commit()

def update_user(username, password, email, confirmemail, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("update given messsage")
    cursor.execute( UPDATE_USER,(username,password,email,confirmemail,uniqueid,))
    db.commit()    

    
