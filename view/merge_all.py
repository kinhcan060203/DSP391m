# import json

# with open('view/data_1.json', 'r', encoding='utf-8') as f1:
#     data_1 = json.load(f1)
# with open('view/data_2.json', 'r', encoding='utf-8') as f2:
#     data_2 = json.load(f2)
# with open('view/track_in4.json', 'r', encoding='utf-8') as f3:
#     track_in4 = json.load(f3)

# data_2_dict = {artist['id_artist']: artist for artist in data_2}
# track_in4_dict = {track['id_track']: track for track in track_in4}

# for track in data_1:
#     id_artist = track['id_artist']
#     id_track = track['id_track']
    
#     # Nếu id_artist có trong top1_50, thêm thông tin vào
#     if id_artist in data_2_dict:
#         track.update(data_2_dict[id_artist])

#     if id_track in track_in4_dict:
#         track.update(track_in4_dict[id_track])    

# # Ghi dữ liệu đã merge vào file mới
# with open(f'view/merged_file.json', 'w', encoding='utf-8') as mf:
#     json.dump(data_1, mf, ensure_ascii=False, indent=4)

import json
with open('view/merged_file.json', 'r', encoding='utf-8') as f1:
    merged_file = json.load(f1)
with open('view/track_in4_release.json', 'r', encoding='utf-8') as f2:
    track_in4_release = json.load(f2)
track_in4_release_dict = {track['id_track']: track for track in track_in4_release}

for track in merged_file:
    id_track = track['id_track']
    if id_track in track_in4_release_dict:
        track.update(track_in4_release_dict[id_track])

with open(f'view/merged_file_all.json', 'w', encoding='utf-8') as mf:
    json.dump(merged_file, mf, ensure_ascii=False, indent=4)