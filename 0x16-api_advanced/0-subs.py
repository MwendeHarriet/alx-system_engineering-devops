#!/usr/bin/python3
"""This script queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an
    invalid subreddit is given, the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    if response.status_code != 200:
        return 0
    else:
        return data['data']['subscribers']
