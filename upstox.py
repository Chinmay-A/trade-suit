import os
import dotenv
import requests

import urllib.parse as parser

dotenv.load_dotenv()

api_key=os.getenv('UPSTOX_KEY')
api_secret=os.getenv('UPSTOX_SECRET')
upstox_id=os.getenv('UPSTOX_ID')
redirecturi='https://127.0.0.1:5000/'

class upstox:

    def __init__(self,apikey,apisecret,upstoxid,redirect_uri):

        self.apikey=apikey
        self.apisecret=apisecret
        self.userid=upstoxid
        self.redirect_uri=redirecturi
        self.auth_token=''
        self.code=''
    
    def login(self):

        authorize_url='https://api.upstox.com/v2/login/authorization/dialog?'
        
        params={
            'client_id':self.apikey,
            'redirect_uri':self.redirect_uri
        }

        query_params=parser.urlencode(params)

        final_authorize_url=authorize_url+query_params

        print("Please Visit: "+final_authorize_url)

        self.code=input("Enter the generated code: ")

        token_url='https://api.upstox.com/v2/login/authorization/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept':'application/json'
        }

        body={
            'code':self.code,
            'client_id': self.apikey,
            'client_secret':self.apisecret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }

        auth_response=requests.post(token_url,headers=headers, data=body)

        if auth_response.status_code==200:
            self.auth_token=auth_response.json().get('access_token')
            print(auth_response.json())
        else:
            print(auth_response.status_code)
        
    def ltp(self,instrument):

        url='https://api.upstox.com/v2/market-quote/ltp'

        headers={
            'Accept':'application/json',
            'Authorization':f'Bearer {self.auth_token}'
        }

        params={
            'instrument_key': instrument
        }

        response=requests.get(url,params=params,headers=headers)

        if response.status_code==200:
            return response.json().get('data').get(instrument).get('last_price')
        else:
            print(response.status_code)
            return -1
    
    def get_historical_data(self,instrument_key,interval,start,end):

        url='https://api.upstox.com/v2/historical-candle/'
        url+=instrument_key+'/'
        url+=interval+'/'
        url+=end+'/'
        url+=start+'/'

        #print(url)

        headers={
            'Accept':'application/json',
            'Authorization':f'Bearer {self.auth_token}'
        }

        response=requests.get(url,headers=headers)

        if response.status_code==200:
            #print(response.json())
            return response.json().get('data').get('candles')
        else:
            print(response.status_code)
            print(response.text)
            return -1





#trial=upstox(apikey=api_key,apisecret=api_secret,upstoxid=upstox_id,redirect_uri=redirecturi)

#trial.get_historical_data('NSE_EQ%7CINE848E01016','30minute','2023-11-13','2023-11-14')
