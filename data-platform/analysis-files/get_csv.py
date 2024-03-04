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

import pandas as pd

query="SELECT * from ongc"

df=pd.DataFrame(sql.connection.cursor().execute(query))

df.to_csv('test_ongc.csv',index=False)