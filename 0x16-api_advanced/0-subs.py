#!/usr/bin/python3
"""How many subs"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Chrome'}

    try:
        response = requests.get(url, headers=headers)

        data = response.json()
        find_subscribers = data.get("data", {}).get("subscribers", 0)
        return find_subscribers
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return 0
        else:
            return 0
