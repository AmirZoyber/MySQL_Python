import re
import mysql.connector
email = input("email : ")
regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
a = mysql.connector.connect(user='amir',password='1234',host='127.0.0.1',database='email')
x = re.search(regex,email)
if x:
    print ("valid email")
else:
    print("invalid email (expression@string.string)")
    email = input("email : ")

password = input("pass : ")
mycursor = a.cursor()
mycursor.execute("INSERT INTO info VALUES (\'%s\',\'%s\')"%(email,password))

a.commit()
mycursor.close()
a.close()

