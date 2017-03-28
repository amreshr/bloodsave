from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy

# Variables that contains the user credentials to access Twitter API
ckey="gD1htH3K7fBXSrHiepeYqoXWz"
csecret="vrLyNmQITu17UBWODs8quGAVHOgslgesdolc9Icy4F5rzVhXwn"
atoken="421846847-IHwrpsRBevYZ5HYtqBCEhr6vklrQf9foq0bPi5W1"
asecret="hpsLkhrGxFhYu4qjq2x01LZag1AQ4YEvGDVw7SWJMjaLB"



# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        json_load = json.loads(data)
        texts = json_load['text']
        coded = texts.encode('utf-8')
        s = str(coded)
        print(s[2:-1])
        return True

    def on_error(self, status):
        print(status)
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

stream = Stream(auth, StdOutListener())

# This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['euro', 'dollar', 'loonie', ], languages=['en'])