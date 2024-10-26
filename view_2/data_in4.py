import json
import base64
import requests

access_token = 'BQCSLoFgXmnMj4SGIVeql4Ud3OC3SnvTu4hFfmpLRpzyjGkh8WQ8jEbQnM-SMei0hl_Rzwv1irE6A5BpMlFctktXBhiu7gNR8pJgcj5r6i5nZYVDaRY'

headers = {
    'Authorization': f'Bearer {access_token}'
}


with open('view_2/views.json', 'r', encoding='utf-8') as f:
    track_in4base_list = json.load(f)

l_track = []
for track_in4 in track_in4base_list:
    id = track_in4['id_track']
    streams = track_in4['streams']

    url = f'https://api.spotify.com/v1/audio-analysis/{id}'
    response = requests.get(url, headers=headers)
    data_raw = response.json()
    data = data_raw['track']

    l_track.append({"id_track": id,
                    "streams": streams,
                    "num_samples": data['num_samples'], 
                    "end_of_fade_in": data['end_of_fade_in'],
                    "start_of_fade_out": data['start_of_fade_out'],
                    "loudness": data['loudness'],
                    "tempo": data['tempo'],
                    "time_signature": data['time_signature'],
                    "key": data['key'],
                    "mode": data['mode']})
    
with open(f'view_2/track_in4.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)

    


