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

takeprofits=[i*0.01 for i in range(1,11)]
stoplosses=[i*0.001 for i in range(5,56,5)]
frequencies=[1,3,5,10,15,30]

net_worths=[]
profits=[]
sharpes=[]
freqs=[]
limlosses=[]
limprofits=[]

sql=sql_helpers.SQL(sqluser,sqlpass,database)


for frequency in frequencies:
    for takeprofit in takeprofits:
        for stoploss in stoplosses:
            
            print("freq: ",frequency)
            backtest=Backtest(Trader,sql,5000,frequency,20,takeprofit,stoploss)
            
            net_worth,profit,sharpe=backtest.start_backtest()
            limlosses.append(stoploss)
            limprofits.append(takeprofit)
            freqs.append(frequency)
            net_worths.append(net_worth)
            profits.append(profit)
            sharpes.append(sharpe)

import pandas as pd

df=pd.DataFrame({
    'frequency':freqs,
    'takeprofit':limprofits,
    'stoploss':limlosses,
    'net_worth': net_worths,
    'profits': profits,
    'sharpe': sharpes
})

df.to_csv('test_results.csv',index=False)