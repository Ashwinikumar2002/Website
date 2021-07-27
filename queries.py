INSERT_INTO_DATABASE= "INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s)"

READ_USER= "SELECT * FROM accounts WHERE uniqueid= % s "

READ_USER_ELITE= "SELECT * FROM accounts WHERE id= % s "

DELETE_USER="DELETE FROM accounts WHERE uniqueid= % s "

UPDATE_USER= "UPDATE accounts SET username=% s,password= % s, email= % s,confirmemail= % s WHERE uniqueid= % s "

LOGIN_USER= "SELECT * FROM accounts WHERE username = % s AND password = % s"

INSERT_INTO_DATABASE_ELITE="INSERT INTO elite VALUES (NULL, % s, % s, % s, % s)"

READ_USER_PREFERENCES="SELECT * FROM preferences WHERE uniqueid = % s"

UPDATE_USER_ELITE= "UPDATE accounts SET education=% s,collegename= % s, branch= % s WHERE uniqueid= % s "

INSERT_INTO_DATABASE_PREFERENCES="INSERT INTO preferences VALUES (NULL, % s, % s, % s, % s, % s)"

UPDATE_USER_PREFERENCES= "UPDATE accounts SET type=% s,stage= % s, companyname= % s, companynotapply= % s, WHERE uniqueid= % s "

INSERT_INTO_DATABASE_EXPERIENCE="INSERT INTO experience VALUES (NULL, % s, % s, % s)"

READ_USER_EXPERIENCE= "SELECT * FROM accounts WHERE id= % s "

UPDATE_USER_EXPERIENCE= "UPDATE accounts SET years=% s,expertise= % s WHERE uniqueid= % s "

INSERT_INTO_DATABASE_CONNECT="INSERT INTO connectaccounts VALUES (NULL, % s, % s, % s)"

READ_USER_CONNECT= "SELECT * FROM accounts WHERE id= % s "