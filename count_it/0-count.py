#!/usr/bin/python3
"""
This script counts occurrences of keywords in Reddit post titles.
"""
from requests import request


def generate_dicts(word_list):
    """
    Generates dictionaries for counting words and handling duplicates.
    
    Args:
        word_list (list): List of words to be counted.
    
    Returns:
        tuple:  A tuple containing two dictionaries:
                - count: Dictionary to store word counts.
                - dup: Dictionary to store duplicates of words.
    """
    count = {k: 0 for k in word_list}
    dup = {}
    for k in word_list:
        if k not in dup:
            dup[k] = 0
        dup[k] += 1
    return (count, dup)


def count_words(subreddit, word_list, after="", count={}, dup={}, init=0):
    """
    Recursively counts occurrences of given keywords in Reddit post titles.

    Args:
        subreddit (str): Name of the subreddit to search.
        word_list (list): List of keywords to count occurrences of.
        after (str): Token for the next page of results (default "").
        count (dict): Dictionary to store word counts (default {}).
        dup (dict): Dictionary to store duplicates of words (default {}).
        init (int): Flag to indicate initialization (default 0).
    """
    if not init:
        count, dup = generate_dicts(word_list)

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        data = response.get('data')
        top = data.get('children')
        _after = data.get('after')

        for item in top:
            data = item.get('data')['title']
            for word in count:
                amount = data.lower().split(' ').count(word.lower())
                count[word] += amount

        if _after:
            count_words(subreddit, word_list, _after, count, dup, 1)
        else:
            sort_abc = sorted(count.items(), key=lambda tup: tup[::-1])
            desc = sorted(sort_abc, key=lambda tup: tup[1], reverse=True)

            for name, cnt in desc:
                cnt *= dup[name]
                if cnt:
                    print('{}: {}'.format(name.lower(), cnt))
    except Exception:
        return None
