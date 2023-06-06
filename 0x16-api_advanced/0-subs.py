#!/usr/bin/python3
"""A function that queries the Reddit API"""


import requests


def number_of_subscribers(subreddit):
    headers= {"User-Agent":"Subreddit Subscriber Counter (by /u/YourUsername)"}

    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            return data["data"]["subscribers"]
        else:
            return 0
    except requests.exceptions.RequestException:

        return 0