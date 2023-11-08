#!/usr/bin/python3
"""Recurse it"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """list containing the titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100\
        '.format(
        subreddit)
    headers = {'User-Agent': 'Chrome'}
    if after:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
            subreddit, after)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])
            for post in children:
                title = post['data']['title']
                hot_list.append(title)
            after = data.get('data').get('after')
            if after:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException as e:
        print(None)
