# import json
# with open('data_popu\merged_data.json', 'r', encoding='utf-8') as f:
#     data_raw = json.load(f)

# for item in data_raw:
#     item.pop("name_track_x", None)
#     item.pop("name_track_y", None)
#     item.pop("name_y", None)

#     #item["name"] = item.pop("name_x")
#     item.pop("name_track_y", None)

#     # Remove dictionaries where all remaining keys have None values
#     keys_to_remove = [key for key, value in item.items() if value is None]
#     # if len(keys_to_remove)>0:
#     #     data_raw.remove(item)

# with open(f'data_popu\merged_data_2.json', 'w', encoding='utf-8') as f:
#     json.dump(data_raw, f, ensure_ascii=False, indent=4)

import json
with open(f'data_popu/merged_data_2.json', 'r', encoding='utf-8') as f:
    data_raw = json.load(f)
print(len(data_raw))
data = [item for item in data_raw if any(value is None for key, value in item.items())]
print(len(data))
result = [item for item in data_raw if item not in data]
print(len(result))
with open(f'data_popu/merged_data_2.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
