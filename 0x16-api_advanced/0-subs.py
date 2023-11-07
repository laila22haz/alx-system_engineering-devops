#!/usr/bin/python3
"""How many subs"""
import requests
import json


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    request = requests.get(url, headers={'User-agent': 'Chrome'})
    json_load = json.loads(request.text)
    if request.status_code == 200:
        find_subscribers = json_load.get("data").get("subscribers")
        return find_subscribers
    else:
        return 0
