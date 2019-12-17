import mysql.connector

#connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",    
    database="datarepresentation"
)

mycursor = mydb.cursor()

createTable = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT)"
mycursor.execute(createTable)
