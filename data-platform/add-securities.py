import os
import dotenv
import sys

dotenv.load_dotenv()
sys.path.append('../')

import sql_connector
import sql_helpers
import upstox

securities_of_interest=[]

sql_user=os.getenv('MYSQL_USER')
sql_pass=ps.getenv('MYSQL_PASS')

upstox_id=os.getenv('UPSTOX_ID')
upstox_key=os.getenv('UPSTOX_KEY')
upstox_secret=os.getenv('UPSTOX_SECRET')
redirect_uri='https://127.0.0.1:5000/'


