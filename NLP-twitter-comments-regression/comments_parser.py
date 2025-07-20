import requests
import pandas as pd
import csv
import json

with open('/Users/vladimirbogatyrev/googleAPI_key.txt', 'r') as api_file:
    API_KEY = api_file.read()
CHANNEL_ID = 'UCXIJgqnII2ZOINSWNOGFThA'
with open('parsed_content/videos.json', 'r') as videos_file:
    videos = json.load(videos_file)
API_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
MAX_RESULTS = 100


output = {
    'commentId' : [],
    'videoId': [],
    'textOriginal': [],
    'likeCount' : [],
    'videoPublishedAt': [],
    'commentPublishedAt': [],
    'commentUpdatedAt': []
}
for video in videos:
    params = {
        'part' : 'id, snippet',
        "videoId": video['videoId'], 
        'order' : 'relevance',
        'maxResults' : MAX_RESULTS,
        'key' : API_KEY

    }

    comments = requests.get(url=API_URL, params=params).json()
    for comment in comments['items']:
        output['commentId'] += [comment['id']]
        output['videoId'] += [video['videoId']]
        output['textOriginal'] += [comment['snippet']['topLevelComment']['snippet']['textOriginal']]
        output['likeCount'] += [comment['snippet']['topLevelComment']['snippet']['likeCount']]
        output['videoPublishedAt'] += [video['videoPublishedAt']]
        output['commentPublishedAt'] += [comment['snippet']['topLevelComment']['snippet']['publishedAt']]
        output['commentUpdatedAt'] += [comment['snippet']['topLevelComment']['snippet']['updatedAt']]

pd.DataFrame.from_dict(output).to_csv('parsed_content/comments.csv', quoting=csv.QUOTE_ALL, escapechar='\\', encoding='utf-8', index=False)
