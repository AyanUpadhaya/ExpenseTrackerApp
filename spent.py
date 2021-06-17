#Expense Tracker App in python 

#step 1 create a database to store expenses
#step 2 create a api functionality

#contact ayanu881@gmail.com

import sqlite3
from datetime import datetime

#create initialization function

def init():
	conn=sqlite3.connect('spent.db')
	#lets create a table

	cur=conn.cursor()

	command="""create table if not exists expenses(amount number,category string, message string, date string);"""

	cur.execute(command)

	conn.commit()

#database created successfully now lets add info

def log(amount,category,message=''):
	#message is optional
	#lets add a date value
	date=str(datetime.now())

	#connect database
	conn=sqlite3.connect('spent.db')
	
	#change command

	cur=conn.cursor()

	command="""insert into expenses values({},'{}','{}','{}');""".format(amount,category,message,date)

	cur.execute(command)

	conn.commit()

# ok now view the database

def view(category=None):
	#connect database
	conn=sqlite3.connect('spent.db')

	cur=conn.cursor()

	if category:
		sql1="""select sum(amount) from expenses where category='{}';""".format(category)
		sql2="""select *from expenses where category='{}';""".format(category)
	else:
		sql1="""select sum(amount) from expenses;"""
		sql2="""select *from expenses;"""
	
	cur.execute(sql1)
	total_amount=cur.fetchone()[0]
	cur.execute(sql2)
	result=cur.fetchall()

	return total_amount, result

#its always good test your code in parts to solve issues
#ok we are done with creating database

