#!/usr/bin/python3
"""How many subs"""
from urllib import request
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = request.urlopen(r)
        if response.getcode() == 200:
            data = response.read().decode('utf-8')
            json_load = json.loads(data)
            find_subscribers = json_load.get("data")["subscribers"]
            return find_subscribers
        else:
            return 0
    except request.HTTPError as e:
        return 0
