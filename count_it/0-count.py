#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
        
    headers = {"User-Agent": "Counting Bot"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts found.")
        return

    data = response.json()
    posts = data['data']['children']
    
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                counts[word] = counts.get(word, 0) + title.count(word)

    next_page = data['data']['after']
    if next_page is not None:
        count_words(subreddit, word_list, next_page, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
