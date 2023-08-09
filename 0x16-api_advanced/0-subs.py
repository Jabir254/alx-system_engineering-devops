#!/usr/bin/python3
"""Returns the number of subcribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit_name):
    """to get the headers and url"""
    headers = {'User-Agent': 'Subreddit Subscribers Counter'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit_name)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
