import mysql.connector as mys

mycon = mys.connect (host='localhost', user='root', passwd='admin', database=' company')
mycursor = mycon.cursor()

print ("Welcome to Employee Data Entry ")a

ans='y'
while ans=='y':
    eno= int (input ("Enter employee no. :"))
    nm = input ("Enter Name :")
    dp = input ("Enter Department :")
    s=int (input ("Enter Salary :"))
    query="insert into emp values ({0}, '{1}', '{2}', {3})". format (eno, nm, dp, s)
    mycursor.execute(query)
    mycon.commit()
    print("##record saved...#")
    ans = input("Do you want to add more?")
