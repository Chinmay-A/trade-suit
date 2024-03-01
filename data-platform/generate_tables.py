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
    query+="(date datetime,time datetime, open float, high float, low float, close float, volume float);"
    print(query)
    return query
