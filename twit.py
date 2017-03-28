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


tweets_data_path ='C:/Users/Amresh/Desktop/PyProj/twitter_dat.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print (len(tweets_data))



tweets = pd.DataFrame()



tweets_by_lang= tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')