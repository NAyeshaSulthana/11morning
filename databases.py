#pmysql---connector which help in making the connections between python and mysql database..

#pip---python packade manager..

#pip install package-name

#pip install pymysql(MySQLdb,mysqlclient,mysql-connector)

import pymysql #connector for connecting python with mysql

conn=pymysql.connect(user="root",password="",host="localhost",database="python10am")
#conn.close()#for closing the mysql connection..

cur=conn.cursor() #creating the cursor for executing the queries in the connection..

#print(cur)

#cur.execute("create database python10am")#Executing mysql queries using python syntax..

#while insert or updating a data commit is mandatory..

#cur.execute("create table emp_details(emp_name varchar(20),emp_designation varchar(20),emp_city varchar(20))")

#cur.execute("insert into emp_details(emp_name,emp_designation,emp_city)values('Ramesh','Developer','Hyderabad')")
#cur.execute("insert into emp_details(emp_name,emp_designation,emp_city)values('suresh','Tester','Chennai')")
#cur.execute("insert into emp_details(emp_name,emp_designation,emp_city)values('Ganesh','Manager','vijayawada')")
#cur.execute("insert into emp_details(emp_name,emp_designation,emp_city)values('mouni','Developer','Hyderabad')")



#print(cur.execute("select * from emp_details"))
#######fetching is for which are already existing before executing....
#print(cur.fetchone())
#print(cur.fetchone())
#print(cur.fetchall())
##################
#for data in cur.fetchall():
	#if data[1]=="Developer":
		#print(data)

#cur.execute("update emp_details set emp_designation='Manager' where emp_designation='Developer'")
#cur.execute("delete from emp_details where emp_name='Ramesh'")
#cur.execute("truncate table emp_details")
#cur.execute("drop table emp_details")
#cur.execute("drop database python10am")
conn.commit()#it is mandatory when we try to update or insert data.

conn.close()#for closing the connection for the database