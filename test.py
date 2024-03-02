import os
import dotenv
import requests

dotenv.load_dotenv()

#url = "https://api.upstox.com/v2/login/authorization/dialog"

#print(os.getenv('UPSTOX_KEY'))

"""url = "https://api.upstox.com/v2/login/authorization/token"

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
