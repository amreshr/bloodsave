
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

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if 'manchester united' in status.text.lower():
            print (status.text)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=["-6.38,49.87,1.77,55.81"])