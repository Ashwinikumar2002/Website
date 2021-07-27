from queries import UPDATE_USER_PREFERENCES
from queries import DELETE_USER
from queries import INSERT_INTO_DATABASE_PREFERENCES, READ_USER_PREFERENCES
from flask import Flask,render_template,request,redirect
from decouple import config
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from queries import *

load_dotenv()
import MySQLdb
import os

def create_user_preferences(type, stage, companyname, companynotapply, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("inside create messsage")
    cursor.execute( INSERT_INTO_DATABASE_PREFERENCES, ( type, stage, companyname, companynotapply, uniqueid ))
    db.commit()
    
def read_user_preferences(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( READ_USER_PREFERENCES , (uniqueid, ))
    preferences = cursor.fetchone()
    return preferences

def delete_user(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( DELETE_USER, (uniqueid, ))
    db.commit()

def update_user_preferences(type, stage, companyname, companynotapply, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("update given messsage")
    cursor.execute( UPDATE_USER_PREFERENCES,(type, stage, companyname, companynotapply, uniqueid))
    db.commit() 
