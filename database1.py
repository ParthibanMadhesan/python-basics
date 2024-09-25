import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bookshop"
)
mycursor=mydb.cursor()
#mycursor.execute("create table Author (Aid int PRIMARY KEY ,AuthorName Varchar(50) unique,Age int DEFAULT(30))")
#mycursor.execute("create table Book(Bid INT PRIMARY KEY, Bname VARCHAR(50),price DOUBLE DEFAULT 350.00,EST_Date DATE,Aid INT,FOREIGN KEY (Aid) REFERENCES Author(Aid))")

# sql="insert into Author(Aid,AuthorName,Age)values(%s,%s,%s)"
# val=[
#      (1,'siva',23),
#      (2,'vicky',25),
#      (3,'sanjay',27)
#     ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print("table created successfully")



# # Define the SQL query to insert values into the Book table
# sql_insert = """
# INSERT INTO Book (Bid, Bname, price, EST_Date, Aid) 
# VALUES (%s, %s, %s, %s, %s)
# """

# # Define the values to be inserted
# val = [
#     (1, 'reactjs', 250.00, '2024-06-24', 1),
#     (2, 'php', 300.00, '2024-06-25', 2),
#     (3, 'electronics', 400.00, '2024-06-26', 3)
# ]

# # Execute the SQL query with executemany()
# mycursor.executemany(sql_insert, val)



# # Commit the transaction to make the changes persistent
# mydb.commit()

# # Print a success message
# print(mycursor.rowcount, "rows inserted into Book table")



# # Close cursor and database connection
# mycursor.close()
# mydb.close()


#dyanic input from user to store values in database

try:
    # Prompt user for input
    num_records = int(input("Enter the number of records you want to insert: "))

    # Prepare to collect values
    val = []
    for i in range(num_records):
        Bid = int(input("Enter Bid: "))
        Bname = input("Enter Bname: ")
        price = float(input("Enter price: "))
        EST_Date = input("Enter EST_Date (YYYY-MM-DD): ")
        Aid = int(input("Enter Aid: "))
        
        # Append values as a tuple
        val.append((Bid, Bname, price, EST_Date, Aid))

    # Define the SQL INSERT statement
    sql_insert = """
    INSERT INTO Book (Bid, Bname, price, EST_Date, Aid) 
    VALUES (%s, %s, %s, %s, %s)
    """

    # Execute the SQL statement
    mycursor.executemany(sql_insert, val)

    # Commit the transaction
    mydb.commit()

    print(mycursor.rowcount, "record(s) inserted successfully.")

except mysql.connector.Error as e:
    print("Error inserting records:", e)

finally:
    # Close cursor and connection
    mycursor.close()
    mydb.close()

