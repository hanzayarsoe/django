import pymysql

db = pymysql.connect(host="localhost", user="root", password="")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# create a database
cursor.execute("CREATE DATABASE mydb")

print('done')