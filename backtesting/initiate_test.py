import os
import dotenv
import sys

sys.path.append('../data-platform/')
sys.path.append('../')

dotenv.load_dotenv()

import sql_helpers
from backtest import Backtest
from trade import Trader

sqluser=os.getenv('MYSQL_USER')
sqlpass=os.getenv('MYSQL_PASS')
database='securities'


sql=sql_helpers.SQL(sqluser,sqlpass,database)
backtest=Backtest(Trader,sql,5000,10,15,0.01,0.005)

backtest.start_backtest()