import requests
import json
import base64

access_token = 'BQAUdD6deDgjh-0UkuwPera077DrHe7Uoy6qclqNyWERCUNXLzNJKKm9DsSPPXvkqDePXRvpomwl80uKAkHrYnf_JH-9DtIuiPa9bl-uSW9mwfnSLec'
#track_ids = set()

headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'market': 'VN'
}

with open('artist_in4/artist_id.json') as f:
    artist_id_list = json.load(f)

l_track=[]
for id in artist_id_list:
    url = f'https://api.spotify.com/v1/artists/{id}/top-tracks'
    response = requests.get(url, headers=headers, params=params)
    data_raw = response.json()
    for data in data_raw['tracks']:
        l_track.append({"id_artist": id, 
                        "id_track": data['id'], 
                        "name_track": data['name'], 
                        "popularity_track": data['popularity'], 
                        "duration_ms": data['duration_ms']})

with open(f'track_in4/track_base_in4.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)