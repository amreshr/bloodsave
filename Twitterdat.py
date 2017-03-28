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

class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API [13.083307, 80.272858,12.08333,80.266667]
#,locations=[-6.38,49.87,1.77,55.81]
    l = StdOutListener()
    
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Blood Donate', 'Need Blood','Emergency blood','Urgently need blood donors','Urgently need blood donor','emergency blood needed'],languages=["en"])
