#!/usr/bin/python3
"""Top Ten"""
import requests

def top_ten(subreddit):
    """Prints the titles of the top ten hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Chrome'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            hot_posts = data.get('data', {}).get('children', [])
            for post in hot_posts[:10]:
                title = post['data']['title']
                print(title)
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
