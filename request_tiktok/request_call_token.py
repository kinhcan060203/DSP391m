import requests
import base64

client_id = 'awbgjm5gecddh9ie'
client_secret = 'VgW7Xs5mmfMjNAbyLLxRzhLHQyRi6yri'

auth_url = 'https://dev.example.com/auth/callback/'
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