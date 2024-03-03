import os
import dotenv
from sql_connector import connectSQL

dotenv.load_dotenv()

SQLUSER=os.getenv('MYSQL_USER')
SQLPASS=os.getenv('MYSQL_PASS')
DB='securities'

connection=connectSQL(SQLUSER,SQLPASS,DB)
cursor=connection.cursor()

def generate_table(security):
    query="CREATE TABLE "+security+" "
    query+="(date VARCHAR(255),time VARCHAR(255), open float, high float, low float, close float, volume float);"
    print(query)
    return query

cursor.execute(generate_table('test'))
