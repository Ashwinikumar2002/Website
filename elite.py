from queries import DELETE_USER, UPDATE_USER_ELITE
from queries import READ_USER_ELITE
from queries import INSERT_INTO_DATABASE_ELITE
from flask import Flask,render_template,request,redirect
from decouple import config
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from queries import *

load_dotenv()
import MySQLdb
import os

def create_user_elite(education , collegename , branch , uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("inside create messsage")
    cursor.execute( INSERT_INTO_DATABASE_ELITE, (education , collegename , branch , uniqueid))
    db.commit()

def read_user_elite(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( READ_USER_ELITE , (uniqueid, ))
    elite = cursor.fetchone()
    return elite

def delete_user(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( DELETE_USER, (uniqueid, ))
    db.commit()

def update_user(username, password, email, confirmemail, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("update given messsage")
    cursor.execute( UPDATE_USER_ELITE,(username,password,email,confirmemail,uniqueid,))
    db.commit()    
