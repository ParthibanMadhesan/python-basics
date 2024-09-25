import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="bookshop"
)

mycursor=mydb.cursor()
# #inner join
# mycursor.execute( """SELECT Book.Bid, Book.Bname, Book.price, Book.EST_Date, Author.AuthorName
# FROM Book
# JOIN Author ON Book.Aid = Author.Aid"""
# )


# #cross join
# mycursor.execute("select Author.* ,Book.* from Author CROSS JOIN Book")


# #equi join
# mycursor.execute("select Author.* ,Book.* from Author , Book WHERE Author.Authorname IN('siva','sanjay') AND Author.Aid=Book.Aid")
# myresult=mycursor.fetchall()


# #inner join
# mycursor.execute("select Author.Authorname,Book.Bid from Author inner join Book ON  Author.Aid=Book.Aid")
# myresult=mycursor.fetchall()

#left join

# mycursor.execute("select Author.Authorname,Book.Bname from Author LEFT JOIN Book ON Author.Aid=Book.Aid")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

#right join
# mycursor.execute("select Book.Bid,Book.Bname,Book.Price,Author.Authorname from Author RIGHT JOIN Book on Author.Aid=Book.Aid")

# myresult=mycursor.fetchall()

# for x in myresult:
#     print(x)

#full join
mycursor.execute("SELECT Book.Bid, Book.Bname, Book.Price, Author.Authorname FROM Author FULL JOIN Book ON Book.Aid = Author.Aid")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)
