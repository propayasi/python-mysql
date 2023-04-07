import mysql.connector as sql
con=sql.connect(host="localhost",password="",user="root")
cursor=con.cursor()
cursor.execute('use db')
#making table
#cursor.execute('create table booksql(book int, name  char(50),price float)')

n=int(input('number of iterations '))
for i in range(n):
   book=int(input('item no'))
   name=input('name')
   price=float(input('price'))
   cursor.execute('insert into booksql values (%s,"%s",%s)'%(book,name,price))
con.commit()

#search
bookid=int(input('bookid'))
cursor.execute("select name from booksql where book=(%s)"%(bookid))
k=cursor.fetchall()
print(k)
#deletion
cursor.execute('delete from booksql where price < 100 ')
cursor.execute('select * from booksql')
p=cursor.fetchall()
print(p)
       
