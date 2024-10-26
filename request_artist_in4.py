import requests
import json
import base64

access_token = 'BQAtaTbKgT3bbcTDsXQeeO8Oe8Gnyrey_8H71hiMmHq4qf2b8U5K-ghlPID2eVx0XnxXlEZ4JGrZJ0p6RADmQUWdnna45b87ICzUqg0XIuWHopVR89s'
artist_ids = set()

headers = {
    'Authorization': f'Bearer {access_token}'
}

with open('artist_in4/artist_id.json') as f:
    artist_id_list = json.load(f)


l_artist = []
for artist_id in artist_id_list[:50]:
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    response = requests.get(url, headers=headers)
    data = response.json()
    l_artist.append({"followers": data['followers']['total'], "genres": data['genres'], "id_artist": artist_id, "name": data['name'], "popularity": data['popularity']})

with open(f'artist_in4/top1_50.json', 'w', encoding='utf-8') as f:
    json.dump(list(l_artist), f, ensure_ascii=False, indent=4)


