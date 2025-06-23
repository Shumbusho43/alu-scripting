#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Print the top 10 hot post titles of a given subreddit"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for i in range(min(10, len(posts))):
            title = posts[i].get('data', {}).get('title')
            print(title)
    except Exception:
        print(None)
