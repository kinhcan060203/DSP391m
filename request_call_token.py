import requests
import base64

# client_id = 'b01ff3eb6d81491ba448907f8294e18a'
# client_secret = 'd09cabb4c646401792ff8f345b6c2153'

client_id = "b99ac867f2f9420786fda349b82828f6"
client_secret = "d4dd707fa4bb4a669c01460b1977ae50"

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

headers = {
    'Authorization': f'Basic {auth_header}'
}

data = {
    'grant_type': 'client_credentials'
}

response = requests.post(auth_url, headers=headers, data=data)
access_token = response.json().get('access_token')
print(access_token)