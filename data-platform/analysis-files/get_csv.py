import os
import dotenv
import sys

dotenv.load_dotenv()
sys.path.append('../')

from sql_helpers import SQL

sql_user=os.getenv('MYSQL_USER')
sql_pass=os.getenv('MYSQL_PASS')
sql_database='securities'

sql=SQL(sql_user,sql_pass,sql_database)
connection=sql.get_connection()
cursor=connection.cursor()

import pandas as pd

cursor.execute("select * from ongc;")
res=cursor.fetchall()
df=pd.DataFrame(res)

df.to_csv('test_ongc.csv',index=False)