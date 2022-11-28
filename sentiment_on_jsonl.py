import re
import os
from datetime import datetime, timedelta
import csv
import json
import flair
import pandas as pd

sentiment_model = flair.models.TextClassifier.load('en-sentiment')

whitespace = re.compile(r"\s+")
web_address = re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
tesla = re.compile(r"(?i)[#@]Tesla(?=\b)")
user = re.compile(r"(?i)@[a-z0-9_]+")



def clean_tweet(tweet):
    word = re.sub(r'[^\x00-\x7f]', "", tweet)
    word = re.sub(r'&gt;', '>', word)
    word = re.sub(r'&lt;', '<', word)
    word = re.sub(r'\u2019', '\'', word)
    word = re.sub(r'\u2014', ',', word)
    word = re.sub(r'\u201c', '"', word)
    word = re.sub(r'\u201d', '"', word)
    word = whitespace.sub(' ', word)
    word = web_address.sub('', word)
    word = tesla.sub('Tesla', word)
    word = user.sub('', word)

    return word


headersCSV = ['created_at','signed_sentiment', 'continuous_sentiment', 'like_count', 'quote_count',
              'reply_count', 'retweet_count',
              'user_verified', 'user_followersCount', 'user_friendsCount', 'user_statusesCount',
              'user_favouritesCount', 'user_listedCount', 'user_mediaCount']

count = 0
with open('from_tesla_tweets_analyzed.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headersCSV)
    writer.writeheader()
    with open("from_tesla_tweets.jsonl", 'r') as json_file:
        for json_str in json_file:
            count = count + 1
            if count % 100 == 0:
                print(count/100)
            result = json.loads(json_str)
            text = clean_tweet(result['content'])

            if text.isspace() or text == "":
                continue

            sentence = flair.data.Sentence(text.strip())
            sentiment_model.predict(sentence)

            score = sentence.labels[0].score  # numerical value 0-1
            sentiment = sentence.labels[0].value  # 'POSITIVE' or 'NEGATIVE'
            continuous_sentiment = score - 0.5
            if sentiment == 'NEGATIVE':
                signed_score = score * -1
                continuous_sentiment = continuous_sentiment * -2
            else:
                signed_score = score
                continuous_sentiment = continuous_sentiment * 2

            writer.writerow({'created_at': result['date'],
                             #'date': filename.name[:-6],
                             'signed_sentiment': signed_score,
                             'continuous_sentiment': continuous_sentiment,
                             'like_count': result['likeCount'],
                             'quote_count': result['quoteCount'],
                             'reply_count': result['replyCount'],
                             'retweet_count': result['retweetCount'],
                             'user_verified': result['user']['verified'],
                             'user_followersCount': result['user']['followersCount'],
                             'user_friendsCount': result['user']['friendsCount'],
                             'user_statusesCount': result['user']['statusesCount'],
                             'user_favouritesCount': result['user']['favouritesCount'],
                             'user_listedCount': result['user']['listedCount'],
                             'user_mediaCount': result['user']['mediaCount']})

# twitter = pd.read_csv('all_tweets_analyzed.csv', index_col=0, parse_dates=['created_at', 'date'])
# print(twitter.dtypes)