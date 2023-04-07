
import mysql.connector as mys

mycon mys.connect (host='localhost', user='root', passwd='admin', database=' company')
mycursor = mycon.cursor ()

d = input ("Enter Department :")
s=int (input ("Enter Salary :"))

query= "select from emp where dept=' (dept) and salary>=(salary)".format (salary=s, dept=d)
mycursor.execute (query)
data = mycursor.fetchall () nrec = mycursor.rowcount
print ("Total records fetched are :",nrec)

if nrec != 0:
    for row in data:
        print(row)
else:
        print ("no suchemployee number")
