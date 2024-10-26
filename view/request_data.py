import json
import base64
import requests

access_token = 'BQBzKJ4qR4oKJE1rEYJz9X2U3zzdRqUs8nyTlR62TI4ZHFWpe94g9QoB2Mu2VyKQAt2VbBQ-r0BCe-MhQVvs6pVEYS0J2vqKyJKFP1WDYNq6I2vTPWQ'

headers = {
    'Authorization': f'Bearer {access_token}'
}


with open('view/viewperw.json', 'r', encoding='utf-8') as f:
    track_in4base_list = json.load(f)

l_track = []
for track_in4 in track_in4base_list:
    id = track_in4['id_track']
    url = f'https://api.spotify.com/v1/tracks/{id}'
    response = requests.get(url, headers=headers)
    data_raw = response.json()
    data_artists = data_raw["artists"]

    l_track.append({"id_track": id,
                    "name_track": data_raw["name"],
                    "duration_ms": data_raw["duration_ms"],
                    "explicit": data_raw["explicit"],
                    "name": data_artists[0]["name"],
                    "id_artist": data_artists[0]["id"]
                    })
    
with open(f'view/data_1.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)