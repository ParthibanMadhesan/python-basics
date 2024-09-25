import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="normalizationdatabase"
)
cursor=mydb.cursor()

# #2-step
# # Create table - Employees (not normalized)
# cursor.execute('''CREATE TABLE Employees (
#                     emp_id INTEGER PRIMARY KEY,
#                     emp_name TEXT NOT NULL,
#                     emp_department TEXT NOT NULL,
#                     emp_salary REAL NOT NULL
#                 )''')

# # Create table - Departments (not normalized)
# cursor.execute('''CREATE TABLE Departments (
#                     dept_id INTEGER PRIMARY KEY,
#                     dept_name TEXT NOT NULL
#                 )''')

# # Commit the transaction
# mydb.commit()



# #step-3

# # Insert data into Employees table
# cursor.execute('''INSERT INTO Employees (emp_id, emp_name, emp_department, emp_salary)
#                   VALUES (1, 'Alice', 'HR', 50000.0)''')
# cursor.execute('''INSERT INTO Employees (emp_id, emp_name, emp_department, emp_salary)
#                   VALUES (2, 'Bob', 'Engineering', 60000.0)''')

# # Insert data into Departments table
# cursor.execute('''INSERT INTO Departments (dept_id, dept_name)
#                   VALUES (1, 'HR')''')
# cursor.execute('''INSERT INTO Departments (dept_id, dept_name)
#                   VALUES (2, 'Engineering')''')

# # Commit the transaction
# mydb.commit()

# #step-4



# # Create a new table - Departments_Normalized (Normalized Departments table)
# cursor.execute('''CREATE TABLE Departments_Normalized (
#                     dept_id INTEGER PRIMARY KEY,
#                     dept_name TEXT NOT NULL
#                 )''')


# # Create a new table - Employees_Normalized (Normalized Employees table)
# cursor.execute('''CREATE TABLE Employees_Normalized (
#                     emp_id INTEGER PRIMARY KEY,
#                     emp_name TEXT NOT NULL,
#                     emp_dept_id INTEGER NOT NULL,
#                     emp_salary REAL NOT NULL,
#                     FOREIGN KEY (emp_dept_id) REFERENCES Departments_Normalized(dept_id)
#                 )''')


# # Insert data into Departments_Normalized table
# cursor.execute('''INSERT INTO Departments_Normalized (dept_id, dept_name)
#                   SELECT dept_id, dept_name FROM Departments''')

# # Update Employees_Normalized table with department IDs
# cursor.execute('''INSERT INTO Employees_Normalized (emp_id, emp_name, emp_dept_id, emp_salary)
#                   SELECT emp_id, emp_name, dept_id, emp_salary
#                   FROM Employees
#                   JOIN Departments ON Employees.emp_department = Departments.dept_name''')

# # Drop old tables
# cursor.execute('''DROP TABLE Employees''')
# cursor.execute('''DROP TABLE Departments''')

# # Commit the transaction
# mydb.commit()


# # Query Employees_Normalized table
# cursor.execute('''SELECT * FROM Employees_Normalized''')
# print("Employees_Normalized table:")
# for row in cursor.fetchall():
#     print(row)

# # Query Departments_Normalized table
# cursor.execute('''SELECT * FROM Departments_Normalized''')
# print("\nDepartments_Normalized table:")

#cursor.execute("select * from Employees order by emp_department limit 2")
cursor.execute('''SELECT dept_name 
FROM (
    SELECT dept_name 
    FROM Departments 
    ORDER BY dept_name DESC 
    LIMIT 2)As subquery
    ORDER BY dept_name ASC
    LIMIT 1;

''')
for row in cursor.fetchall():
    print(row)


