import MySQLdb
# Open database connection ( If database is not created don't give dbname)
db = MySQLdb.connect("localhost","root","","demo" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# For creating create db
# Below line  is hide your warning 
cursor.execute("SET sql_notes = 0; ")
# create db here....
cursor.execute("create database IF NOT EXISTS parkingDb")
# create table
cursor.execute("SET sql_notes = 0; ")
cursor.execute("create table IF NOT EXISTS user (username varchar(70),password varchar(20), mobile_no varchar(20), address varchar(512));")
cursor.execute("SET sql_notes = 1; ")
#insert data
cursor.execute("insert into user values('admin','pass', "9988998899", "Kesnand, wagholi")")
# Commit your changes in the database
db.commit()
# disconnect from server
db.close()
