import requests
import json
import base64

access_token = 'BQCmYQPFHAVd8wlA0_G6E_YZzGY0EmwkwU6EOWLuKDmFKYCG4melEaMeTXe3y4HkDAFNOweHlRSK0sTDDKhXp7uGnyMLJ6zPt-qGvJZ7DeBZF19oiFc'
artist_ids = set()

headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'market': 'VN'
}

with open('playlists_id.json') as f:
    playlist_id_list = json.load(f)
i=0
for playlist_id in playlist_id_list:
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    artist_ids = set()
    try:
        for item in data['items']:
            for artist in item['track']['artists']:
                artist_ids.add(artist['id'])

        with open(f'artist_id/artist_id{i}.json', 'w') as f:
            json.dump(list(artist_ids), f)
            i+=1
    except:
        print("hehe")
