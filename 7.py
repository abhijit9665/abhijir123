# import re
# result = re.findall('hello', 'hello world hellos ')
# print(result) # Output: ['hello', 'world']
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="myusername",password="mypassword")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
