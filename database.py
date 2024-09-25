import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="pythondata"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE customer(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),address VARCHAR(255))")
#mycursor.execute("INSERT INTO customer(name,address) VALUES('parth','dharmapuri')")
#mycursor.execute("ALTER TABLE customer ADD COLUMN dept VARCHAR(255)")
#mycursor.execute("update customer set dept='sales'")
#mycursor.execute("delete from customer where name='parth'")
#mycursor.execute("show databases")

#mycursor.execute("select * from customer")

# mycursor.execute("select name,address from customer where id=3")

# myresult=mycursor.fetchall()

# for x in myresult:
#   print(x)
#mydb.commit()
