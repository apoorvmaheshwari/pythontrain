import pymysql

db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor(pymysql.cursors.DictCursor)
data = cursor.execute("""Select * from employee """)

# db.commit()
resp = cursor.fetchall()
print(resp)
# for row in resp:
#     print(row["fname"], row["lname"])
db.close()

'''
cursor.execute("SELECT * FROM sample")
rows= cursor.rowcount
results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
	  print('fname: {0}, lname: {1}'.format(fname,lname))
db.commit()
db.close()

'''

"""CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

"""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME)
         VALUES ('Mac', 'Mohan')"""
