import requests

# Thay thế bằng Access Token của bạn
access_token = 'b6b6c91ecc9d61d30ef12aa403e1e6a7ac7d924b'

# URL giả định cho API lấy thông tin âm thanh trending
url = 'https://open-api.tiktok.com/user/info/'

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    trending_sounds = response.json()
    print(trending_sounds)
else:
    print(f'Error: {response.status_code} - {response.text}')