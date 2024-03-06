import os
import dotenv

import upstox_client as upstox
from upstox_client.rest import ApiException

dotenv.load_dotenv()

connection=upstox.LoginApi()

code=''
apikey=os.getenv('UPSTOX_KEY')
apisecret=os.getenv('UPSTOX_SECRET')
redirect_uri='https://127.0.0.1:5000/'
grant_type='authorization_code'

try:
    # Get token API
    api_response = connection.token(code='6UAD9K',api_version='3.0',client_id='6UAD9K', client_secret=apikey,
                                      redirect_uri=redirect_uri, grant_type=grant_type)
    print(api_response)
except ApiException as e:
    print(e)




"""import requests

dotenv.load_dotenv()

#url = "https://api.upstox.com/v2/login/authorization/dialog"

#print(os.getenv('UPSTOX_KEY'))

url = "https://api.upstox.com/v2/login/authorization/token"

payload={
    'code':'mgDZPL',
    'client_id': os.getenv('UPSTOX_KEY'),
    'client_secret': os.getenv('UPSTOX_SECRET'),
    'redirect_uri':'https://127.0.0.1:5000/',
    'grant_type': 'authorization_code'
}
params = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

response = requests.request("POST", url, params=params, data=payload)

print(response.text)"""
