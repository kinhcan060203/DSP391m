import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
from datetime import datetime

async def fetch(url, session):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.text()

def extract_video_id(input_string):
    pattern = r'"videoId":"([^"]+)"'
    matches = re.findall(pattern, input_string)
    return matches

async def extract_script(url, session):
    try:
        html_content = await fetch(url, session)
        soup = BeautifulSoup(html_content, 'html5lib')
        span_tags = soup.find_all('script')
        
        if span_tags and len(span_tags) > 23:
            video_id = extract_video_id(str(span_tags[23]))
            if video_id:
                return video_id[1] 
        return None
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None

async def get_youtube_video_details(video_id, api_key, session):
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=id,snippet,statistics"
    response = await fetch(url, session)
    return response

async def process_item(item, api_key, session):
    id_artist = item['id_artist']
    id_track = item['id_track']
    name_track = item['name_track']
    name_artist = item['name']
    query = f"{name_track} - {name_artist}"
    print(f"Processing Track: {name_track}, Artist: {name_artist}")

    video_id = await extract_script(f'https://www.youtube.com/results?search_query={"+".join(query.split())}', session)
    
    if video_id:
        video_details_json = await get_youtube_video_details(video_id, api_key, session)
        
        if video_details_json:
            data = json.loads(video_details_json)
            if 'items' in data and len(data['items']) > 0:
                video_details = data['items'][0]
                publish_time = video_details['snippet']['publishedAt']
                publish_time = datetime.strptime(publish_time, '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%Y')
                
                statistics = video_details.get('statistics', {})
                return {
                    "video_id": video_details['id'],
                    "id_artist": id_artist,
                    "id_track": id_track,
                    "name": name_artist,
                    "name_track": name_track,
                    "publish_time": publish_time,
                    **statistics
                }
    return None

async def main(api_key):
    updated_data = []
    
    async with aiohttp.ClientSession() as session:
        with open('dsp/data-view-month-1k.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(f"Number of items: {len(data)}")
        
        tasks = []
        for item in data:
            task = process_item(item, api_key, session)
            tasks.append(task)
            
            if len(tasks) == 100: 
                results = await asyncio.gather(*tasks)
                updated_data.extend([result for result in results if result is not None])
                tasks = []  
                with open('songs_3.json', 'w', encoding='utf-8') as file:
                    json.dump(updated_data, file, ensure_ascii=False, indent=4)
        if tasks:
            results = await asyncio.gather(*tasks)
            updated_data.extend([result for result in results if result is not None])

        with open('songs_1.json', 'w', encoding='utf-8') as file:
            json.dump(updated_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    api_key = 'AIzaSyC2ljKF3qMKNTqxHQNP-uzPV5VCoOGyK9Q' 
    asyncio.run(main(api_key))