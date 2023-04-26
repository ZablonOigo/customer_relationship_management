import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass123'
)

#prepare a cursor object
cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE customer")
print('all done ')