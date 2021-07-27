from queries import UPDATE_USER_EXPERIENCE
from queries import DELETE_USER
from app import experience
from queries import READ_USER_EXPERIENCE
from queries import INSERT_INTO_DATABASE_EXPERIENCE
from flask import Flask,render_template,request,redirect
from decouple import config
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from queries import *

load_dotenv()
import MySQLdb
import os

def create_user_experience(years, expertise, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("inside create message")
    cursor.execute( INSERT_INTO_DATABASE_EXPERIENCE, (years, expertise, uniqueid))
    db.commit()
    
def read_user_experience(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( READ_USER_EXPERIENCE , (uniqueid, ))
    experience = cursor.fetchone()
    return experience

def delete_user_experience(uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    cursor.execute( DELETE_USER, (uniqueid, ))
    db.commit()

def update_user_experience(years, expertise, uniqueid):
    db = MySQLdb.connect(os.getenv('MYSQL_HOST'),os.getenv('MYSQL_USER'),os.getenv('MYSQL_PASSWORD'),os.getenv('MYSQL_DB') )
    cursor = db.cursor()
    print("update given message")
    cursor.execute( UPDATE_USER_EXPERIENCE,(years, expertise, uniqueid,))
    db.commit()    