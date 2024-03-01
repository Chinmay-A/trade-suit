import os
import dotenv
from sql_connector import connectSQL

dotenv.load_dotenv()

SQLUSER=os.getenv('MYSQL_USER')
SQLPASS=os.getenv('MYSQL_PASS')
DB='securities'

connection=connectSQL(SQLUSER,SQLPASS,DB)
cursor=connection.cursor()

