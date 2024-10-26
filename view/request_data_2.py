import json
import base64
import requests

access_token = 'BQBzKJ4qR4oKJE1rEYJz9X2U3zzdRqUs8nyTlR62TI4ZHFWpe94g9QoB2Mu2VyKQAt2VbBQ-r0BCe-MhQVvs6pVEYS0J2vqKyJKFP1WDYNq6I2vTPWQ'

headers = {
    'Authorization': f'Bearer {access_token}'
}


with open('view/data_1.json', 'r', encoding='utf-8') as f:
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
    
with open(f'view/data_2.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)