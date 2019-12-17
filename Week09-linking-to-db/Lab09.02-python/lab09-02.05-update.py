import mysql.connector

#connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",    
    database="datarepresentation"
)

mycursor = mydb.cursor()

update="update student set name= %s, age= %s where id= %s"
values = ("Joe",33, 1)
mycursor.execute(update, values)
mydb.commit()
print("Data updated")