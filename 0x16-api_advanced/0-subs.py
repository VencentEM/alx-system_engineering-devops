#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests

BASE_URL = 'https://www.reddit.com'

def number_of_subscribers(subreddit):
    api_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    try:
        res = requests.get(
            f'{BASE_URL}/r/{subreddit}/about.json',
            headers=api_headers,
            timeout=10
        )
        res.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = res.json()
        return data['data']['subscribers']
    except requests.RequestException as e:
        print(f"Error retrieving data: {e}")
        return 0
    except KeyError:
        print("Subreddit not found or data format is unexpected.")
        return 0

# Example usage
subreddit_name = 'python'
print(f"Number of subscribers in r/{subreddit_name}: {number_of_subscribers(subreddit_name)}")
