import sqlite3

#executes script "tables" located in the SQLDatabase folder. It Will destroy all database tables and reinstall everything.
# User data is lost, Warning
connectionName = "sepdb.db"
connection = sqlite3.connect(connectionName)
cursor = connection.cursor()
cursor.executescript(open('./SQLDatabase/tables', 'r').read())
connection.commit()
connection.close()
