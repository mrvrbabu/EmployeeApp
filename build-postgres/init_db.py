import os 
import psycopg2 

# Make sure the database 'factory' is already created 

conn = psycopg2.connect(
        host='localhost', 
        database='factory', 
        user='postgres',
        password='postgres'
)

# Open a cursor to perform database operations 
cur = conn.cursor()

# Execute a command, this creates a new table 
cur.execute('DROP TABLE IF EXISTS employees;')
cur.execute('CREATE TABLE employees(emp_id serial PRIMARY KEY,'
             'emp_fname varchar (10) NOT NULL,'
             'emp_lname varchar (10) NOT NULL,'
             'emp_dob date,' 
             'emp_doj date,'
             'salary integer);'
            )

cur.execute('INSERT INTO employees (emp_id, emp_fname, emp_lname, emp_dob, emp_doj, salary)'
            'VALUES(%s, %s, %s, %s, %s, %s)',
            (10001, 
             'Vinay',  
             'Kumar', 
             '2001-04-01', 
             '2021-01-15', 
             5000)
            )
conn.commit()
cur.close()
conn.close()

# Insert data into employees using below command to be executed inside psql commandline 
# factory=# \i /home/rbabu/EmployeeApp/employee_data.sql 
