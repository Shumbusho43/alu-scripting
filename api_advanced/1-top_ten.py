#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if the request was successful
        if RESPONSE.status_code != 200:
            print(None)
            return
        
        # Parse JSON response
        data = RESPONSE.json()
        
        # Validate the response structure
        if not data or not isinstance(data, dict):
            print(None)
            return
        
        # Check if 'data' key exists and has 'children'
        if 'data' not in data or not data['data'] or 'children' not in data['data']:
            print(None)
            return
        
        HOT_POSTS = data['data']['children']
        
        # Check if we have posts
        if not HOT_POSTS:
            print(None)
            return
        
        # Print the titles
        for post in HOT_POSTS:
            if post and 'data' in post and 'title' in post['data']:
                print(post['data']['title'])
            
    except Exception:
        print(None)
