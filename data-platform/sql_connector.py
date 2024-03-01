import mysql.connector as mysql

def connectSQL(username,password,db):
    connection=mysql.connect(username=username,password=password,host='localhost',database=db)
    print("connected to mysql with user: "+username+"@localhost")
    return connection