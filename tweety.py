import json
import pandas as pd
import matplotlib.pyplot as plt
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
ckey="gD1htH3K7fBXSrHiepeYqoXWz"
csecret="vrLyNmQITu17UBWODs8quGAVHOgslgesdolc9Icy4F5rzVhXwn"
atoken="421846847-IHwrpsRBevYZ5HYtqBCEhr6vklrQf9foq0bPi5W1"
asecret="hpsLkhrGxFhYu4qjq2x01LZag1AQ4YEvGDVw7SWJMjaLB"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)


#api.get_status(id=683046767231766528)
#api.retweet(id=683046767231766528) retweets the tweet
#api.lookup_users=(user_ids="amyress")
#api.update_status('@iamanish My status update', 845931203265908736)reply to tweets
for page in tweepy.Cursor(api.user_timeline, id="421846847").pages(1):
    for item in page:
        if item.in_reply_to_user_id_str == "97948029":
            last_tweet = item

#updates pic in tweitter api.update_with_media("watch.jpg")

