#!/usr/bin/python3
"""Prints the first 10 hot posts listed for a given subreddit"""


import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Top Ten Post Printer (by /u/YourUsername)"}

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        response = requests.get(url, headers=headers)

        # check if the response is successful
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                title = post["data"]["title"]
                print(title)

        else:
            print(None)

    except requests.exceptions.RequestException:
        print(None)
