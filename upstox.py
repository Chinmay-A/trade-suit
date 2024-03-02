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
        self.authtoken=''
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


#trial=upstox(apikey=api_key,apisecret=api_secret,upstoxid=upstox_id,redirect_uri=redirecturi)

#trial.login()
