import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

SQLUSER=os.getenv('MYSQL_USER')
SQLPASS=os.getenv('MYSQL_PASS')

connection=mysql.connect(username=SQLUSER,password=SQLPASS,host='localhost',database='cryptos')

db=connection.cursor()

sql_query="CREATE TABLE coins( coin VARCHAR(255), time int, date date, open float, close float, high float, low float, volume float);"

db.execute(sql_query)