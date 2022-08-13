import mysql.connector
Database = mysql.connector.connect(
  host="localhost",
  user="root",
  database="myboat"
)
Cursor = Database.cursor()