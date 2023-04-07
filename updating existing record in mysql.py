import mysql.connector as mys

mycon mys.connect (host='localhost', user='root', passwd='admin', database=' company')
mycursor = mycon.cursor()

print ("Welcome to Employee Update Screen ")
eno = int(input ("Enter employee number :"))

query= "select from emp where empno={}".format (eno)
mycursor.execute(query)
data = mycursor.fetchone()

if data!=None:
    print ("## Record Found Details are ##")
    print (data)
    ans = input ("Are you sure to update Salary : (y/n)")
    if ans=='y':
        s = int(input ("Enter new Salary :"))
        query="update emp set salary={} where empno={}".format (s, eno)
        mycursor.execute(query)
        mycon.commit()
        print("##Record found##)
else:
        print("no such employee number exists")

mycon.close()
