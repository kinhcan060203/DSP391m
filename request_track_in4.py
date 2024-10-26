import json
import base64
import requests

access_token = 'BQDINwMcIv1yPo3msMVEv0l5nY-REZUcrs9NvaOL2rnb3xgTieYw6cOL9oauA2FQvAg6QC5v_35f2BqHona1Wbpi4sZSUfH1ocLA6f1RqXiNGm1i-Yg'

headers = {
    'Authorization': f'Bearer {access_token}'
}


with open('track_in4/track_base_in4.json', 'r', encoding='utf-8') as f:
    track_in4base_list = json.load(f)

l_track = []
for track_in4 in track_in4base_list[:100]:
    id = track_in4['id_track']
    name = track_in4['name_track']
    url = f'https://api.spotify.com/v1/audio-analysis/{id}'
    response = requests.get(url, headers=headers)
    data_raw = response.json()
    data = data_raw['track']

    l_track.append({"id_track": id,
                    "name_track": name,
                    "num_samples": data['num_samples'], 
                    "end_of_fade_in": data['end_of_fade_in'],
                    "start_of_fade_out": data['start_of_fade_out'],
                    "loudness": data['loudness'],
                    "tempo": data['tempo'],
                    "time_signature": data['time_signature'],
                    "key": data['key'],
                    "mode": data['mode']})
    
with open(f'track_in4/track_expert_in4_500.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)

    


