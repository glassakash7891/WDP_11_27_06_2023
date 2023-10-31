import mysql.connector as sql

akash=sql.connect(host="localhost",user="root",password="root",port=3306,database="wd12")
car=akash.cursor()
print("database connected")