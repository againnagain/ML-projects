import requests
import json


with open('/Users/vladimirbogatyrev/googleAPI_key.txt', 'r') as api_file:
    API_KEY = api_file.read()
CHANNEL_ID = 'UCXIJgqnII2ZOINSWNOGFThA'
API_URL = 'https://www.googleapis.com/youtube/v3/search'
MAX_RESULTS = 50
OUTPUT_FILE = "parsed_content/videos.json"

params = {
    'part': 'snippet',
    'channelId': CHANNEL_ID,
    'maxResults': MAX_RESULTS,
    'order': 'viewCount',
    'type': 'video',
    'key': API_KEY
}

request_json = requests.get(url=API_URL, params=params).json()
videos_data = []
for item in request_json['items']:
    videos_data.append({
        'videoId': item['id']['videoId'],
        'videoPublishedAt': item['snippet']['publishedAt']
    })

with open('parsed_content/videos.json', 'w') as f:
    json.dump(videos_data, f, ensure_ascii=False, indent=4)

