#!/usr/bin/python3
"""How many subs"""
import requests


def top_ten(subreddit):
    """return the Top ten"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Chrome'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        hot_posts = data.get('data', {}).get('children', [])
        for post in hot_posts[:10]:
            title = post['data']['title']
            print(title)
    else:
        print(None)
