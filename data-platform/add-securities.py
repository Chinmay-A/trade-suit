import os
import dotenv
import sys

dotenv.load_dotenv()
sys.path.append('../')

import sql_connector
import sql_helpers
import upstox

securities_of_interest=['IDBI','ONGC','HINDZINC','VEDL','IRFC']

sql_user=os.getenv('MYSQL_USER')
sql_pass=os.getenv('MYSQL_PASS')
sql_database='securities'

upstox_id=os.getenv('UPSTOX_ID')
upstox_key=os.getenv('UPSTOX_KEY')
upstox_secret=os.getenv('UPSTOX_SECRET')
redirect_uri='https://127.0.0.1:5000/'


sql=sql_helpers.SQL(sql_user,sql_pass,sql_database)

for security in securities_of_interest:
    print("Adding the table for security: "+security)
    sql.add_table(security)

upstoxc=upstox.upstox(upstox_key,upstox_secret,upstox_id,redirect_uri)
#upstoxc.login()

instument_mapping={
    'IDBI':'NSE_EQ|INE008A01015',
    'ONGC':'NSE_EQ|INE213A01029',
    'HINDZINC': 'NSE_EQ|INE267A01025',
    'VEDL': 'NSE_EQ|INE205A01025',
    'IRFC':'NSE_EQ|INE053F01010'



}

for instrument in securities_of_interest:

    current_security_data=upstoxc.get_historical_data(instument_mapping[instrument],'1minute','2023-10-01','2024-03-01')
    print(type(current_security_data))

    for candle in current_security_data:
        candle_data=[]
        candle_data.append(candle[0][0:10])
        candle_data.append(candle[0][11:19])
        candle_data.append(candle[1])
        candle_data.append(candle[2])
        candle_data.append(candle[3])
        candle_data.append(candle[4])
        candle_data.append(candle[5])

        print("Adding for Instrument: "+instrument+" "+candle_data[0]+"@"+candle_data[1])
        sql.add_data(instrument,candle_data)