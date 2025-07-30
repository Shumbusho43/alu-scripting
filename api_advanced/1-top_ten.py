#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code == 200:
            data = RESPONSE.json()
            if (data and 'data' in data and data['data'] and
                    'children' in data['data']):
                HOT_POSTS = data['data']['children']
                for post in HOT_POSTS:
                    if (post and 'data' in post and
                            'title' in post['data']):
                        print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
