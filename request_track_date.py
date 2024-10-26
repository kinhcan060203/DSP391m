import requests
import json
import base64

access_token = 'BQBMuNmVkoMWRKtsZqRmNMrTAnsTDL7sa3te5j8VydENTUYKYa22YZ6no-kdr7ouUFueeIWYAoSyOCe4n5aiz6Ho525GUu1CJHloYEtJkD_v2vbUX3g'
#track_ids = set()

headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'market': 'VN'
}

with open('view/viewperw.json', 'r', encoding='utf-8') as f:
    track_in4base_list = json.load(f)

l_track=[]
for track_in4 in track_in4base_list:
    id = track_in4['id_track']
    url = f'https://api.spotify.com/v1/tracks/{id}'
    response = requests.get(url, headers=headers, params=params)
    data_raw = response.json()
    data = data_raw['album']

    l_track.append({"id_track": id,
                    "release_date": data['release_date']})

with open(f'view/track_in4_release.json', 'w', encoding='utf-8') as f:
    json.dump(l_track, f, ensure_ascii=False, indent=4)