import requests
import base64
import json
access_token = 'BQCmYQPFHAVd8wlA0_G6E_YZzGY0EmwkwU6EOWLuKDmFKYCG4melEaMeTXe3y4HkDAFNOweHlRSK0sTDDKhXp7uGnyMLJ6zPt-qGvJZ7DeBZF19oiFc'
search_url = 'https://api.spotify.com/v1/search'
headers = {
    'Authorization': f'Bearer {access_token}'
}

params = {
    'q': 'RPT MCK',
    'type': 'artist',
    'market': 'VN',
    'limit' : 3,
    'offset': 1
}

response = requests.get(search_url, headers=headers, params=params)
data = response.json()
print(data)

# url = 'https://api.spotify.com/v1/browse/featured-playlists'
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }
# params = {
#     'country': 'VN',
#     'limit': 10
# }
# response = requests.get(url, headers=headers, params=params)
# data = response.json()

# playlist_ids = set()
# for i in data['playlists']['items']:
#     playlist_ids.add(i['id']) # find playlist hot to find artists

# with open('playlists_id.json', 'w') as f:
#     json.dump(list(playlist_ids), f)