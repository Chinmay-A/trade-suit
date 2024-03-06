import os
import dotenv
import sys

import sql_helpers

dotenv.load_dotenv()

sql_user=os.getenv('MYSQL_USER')
sql_pass=os.getenv('MYSQL_PASS')
sql_database='securities'

sql=sql_helpers.SQL(sql_user,sql_pass,sql_database)


results= sql.get_securities()

print(results)
#print(results)