import oauth2 as oauth
import json
import pandas as pd
CONSUMER_KEY = "xxxxXXXXXXxxxXXX"
CONSUMER_SECRET = "xxxxXXXXXXxxxXXX"
ACCESS_KEY = "xxxxXXXXXXxxxXXX-xxxxXXXXXXxxxXXX"
ACCESS_SECRET = "xxxxXXXXXXxxxXXX"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)
hashtag = input("Hashtag?: ")
query = "https://api.twitter.com/1.1/search/tweets.json?q=%23" + hashtag +"&count=200"
response, data = client.request(query)
tweets = json.loads(data)


screen_name = list()
for tweet in tweets['statuses']:
    print(tweet['user']['name'] + ":\n" + tweet['text'])
    print("\n\n")

