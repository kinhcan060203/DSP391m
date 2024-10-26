import json
import base64
import requests

access_token = 'BQDRBUpUSth6UDrlCFW7_VnwnpCh8JRfdCS8BWhJtlhk9CFsj56B1wMRUOM-LQwYpNaUUryHa3LLpJ-Ib7oYNuwZ_XreMBl96HFaq45Fkyv6lG8HG-E'

headers = {
    'Authorization': f'Bearer {access_token}'
}


with open('view_2/views.json', 'r', encoding='utf-8') as f:
    track_in4base_list = json.load(f)

l_track = []
for track_in4 in track_in4base_list:
    id = track_in4['id_track']
    url = f'https://api.spotify.com/v1/tracks/{id}'
    response = requests.get(url, headers=headers)
    data_raw = response.json()
    data_artists = data_raw["artists"]
    data_date = data_raw['album']

    l_track.append({"id_track": id,
                    "name_track": data_raw["name"],
                    "duration_ms": data_raw["duration_ms"],
                    "explicit": data_raw["explicit"],
                    "name": data_artists[0]["name"],
                    "id_artist": data_artists[0]["id"],
                    "release_date": data_date['release_date']
                    })
    
with open(f'view_2/data_1.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)