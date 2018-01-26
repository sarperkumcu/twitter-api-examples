#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:14:06 2018

@author: sarper
"""

import oauth2 as oauth
import json
import pandas as pd
import datetime
import pymongo
from pymongo import MongoClient
from pprint import pprint
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
#client = MongoClient()
#db = client.twitterDatas

#twitterPosts = db.twitterPosts
#post_id = db.twitterPosts.insert_many(json.loads(data))


for tweet in tweets:
            print (tweet['text'])

