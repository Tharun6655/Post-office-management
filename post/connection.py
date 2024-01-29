import mysql.connector

con=mysql.connector.connect(host='localhost',username='root',password='password',database='simple')
my_cursor=con.cursor()

con.commit()
con.close()
print("connection sucesfully connected")