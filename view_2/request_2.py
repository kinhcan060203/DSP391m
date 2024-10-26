import json
import base64
import requests

access_token = 'BQDhpqCXpdzTaOsu4w_G9M7fyGSm8j7eU0HP4ACP3C8HISQcMXt3I0APha9LzFZakOcBjSCIuTTL1308DC6dx1s0TMAj8qEgoXFbW2qL9-1ILmTRe30'

headers = {
    'Authorization': f'Bearer {access_token}'
}


with open('view_2\data_1.json', 'r', encoding='utf-8') as f:
    track_in4base_list = json.load(f)

l_track = []
for track_in4 in track_in4base_list:
    id = track_in4['id_artist']
    url = f'https://api.spotify.com/v1/artists/{id}'
    response = requests.get(url, headers=headers)
    data_raw = response.json()

    l_track.append({"id_artist": id,
                    "popularity": data_raw["popularity"],
                    "followers": data_raw['followers']['total']
                    })
    
with open(f'view_2/data_2.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)