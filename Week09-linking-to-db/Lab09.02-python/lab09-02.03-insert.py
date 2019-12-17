import mysql.connector

#connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",    
    database="datarepresentation"
)

mycursor = mydb.cursor()

insertData = "insert into student (name, age) values (%s, %s)"
values = ('Mary', 19)
mycursor.execute(insertData, values)