import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

SQLUSER=os.getenv('MYSQL_USER')
SQLPASS=os.getenv('MYSQL_PASS')

def connectSQL():
    connection=mysql.connect(username=SQLUSER,password=SQLPASS,host='localhost',database='cryptos')
    print("connected to mysql with user: "+SQLUSER+"@localhost")
    return connection