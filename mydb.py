import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '@Sidhuwalker1'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Check if the database exists before creating it
try:
    cursorObject.execute("CREATE DATABASE sidhant")
except mysql.connector.errors.DatabaseError as err:
    if err.errno == 1007:  # Error code for "database exists"
        print("Database 'sidhant' already exists.")
    else:
        raise  # Re-raise the exception if it's a different error

print("All Done!")