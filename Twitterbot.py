from __future__ import absolute_import, print_function
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from twit import sortdata
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):

        b = json.loads(data)['text']
        if(sortdata(b)):

            conv_string = str(data)
            clean_txt = tokenizer.tokenize(conv_string)
            print(clean_txt)
            nameindex = clean_txt.index('screen_name')
            
            api.update_status("Hey @" +clean_txt[nameindext8 + 1]+ " DM us for donors" + " twitter.com/messages/compose?recipient_id=880311983219777538&text=Hey",
                              in_reply_to_status_id=clean_txt[10])

        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    stream = Stream(auth, l)
    stream.filter(track=['Need Blood','Blood Group'])









