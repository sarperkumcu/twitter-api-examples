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
user_name = input("User name?: ")
query = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + user_name + "&count=200"
response, data = client.request(query)
tweets = json.loads(data)


screen_name = list()
for tweet in tweets:
    for mentions in tweet['entities']['user_mentions']:
    	print(mentions['screen_name'])
    	screen_name.append(mentions['screen_name'])

df = pd.Series( (v for v in screen_name) )
df.value_counts()[:20].plot(kind='barh')
