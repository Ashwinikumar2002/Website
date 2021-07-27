DROP DATABASE Flask;

CREATE DATABASE flask;

use flask;

CREATE TABLE accounts(
   id int(11) NOT NULL AUTO_INCREMENT,
   username varchar(255) NOT NULL,
   password varchar(255) NOT NULL,
   email varchar(255) NOT NULL,
   confirmemail varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE elite(
   id int(11) NOT NULL AUTO_INCREMENT,
   education varchar(255) NOT NULL,
   collegename varchar(255) NOT NULL,
   branch varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE preferences(
   id int(11) NOT NULL AUTO_INCREMENT,
   type varchar(255) NOT NULL,
   stage varchar(255) NOT NULL,
   companyname varchar(255) NOT NULL,
   companynotapply varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE experience(
   id int(11) NOT NULL AUTO_INCREMENT,
   years int NOT NULL,
   expertise varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE connectaccounts(
   id int(11) NOT NULL AUTO_INCREMENT,
   linkedin varchar(255) NOT NULL,
   github varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE yourpreferences(
   id int(11) NOT NULL AUTO_INCREMENT,
   salary int NOT NULL,
   corecompetency varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE professionaldetails(
   id int(11) NOT NULL AUTO_INCREMENT,
   phonenumber int NOT NULL,
   designation varchar(255) NOT NULL,
   companyname varchar(255) NOT NULL,
   expectedsalary int NOT NULL,
   availablein int NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE resetpassword(
   id int(11) NOT NULL AUTO_INCREMENT,
   newpassword varchar(255) NOT NULL,
   confirmnewpassword varchar(255) NOT NULL,
   uniqueid varchar(255) NOT NULL,
   PRIMARY KEY(id)
);
