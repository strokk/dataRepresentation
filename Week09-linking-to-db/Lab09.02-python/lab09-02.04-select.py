import mysql.connector

#connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",    
    database="datarepresentation"
)

mycursor = mydb.cursor()

select="select * from student where id = %s"
values = (1,)
mycursor.execute(select, values)
result = mycursor.fetchall()
for i in result:
    print(i)