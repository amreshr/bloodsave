
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import Stream

#from our keys module (keys.py), import the keys dictionary
#from keys import keys



#consumer key, consumer secret, access token, access secret.
ckey="gD1htH3K7fBXSrHiepeYqoXWz"
csecret="vrLyNmQITu17UBWODs8quGAVHOgslgesdolc9Icy4F5rzVhXwn"
atoken="421846847-IHwrpsRBevYZ5HYtqBCEhr6vklrQf9foq0bPi5W1"
asecret="hpsLkhrGxFhYu4qjq2x01LZag1AQ4YEvGDVw7SWJMjaLB"
     
auth =tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
twts = api.search(q="Hi")

#list of specific strings we want to check for in Tweets
t = ['hi','hello','#throwback','#selfie','#tbt']
 
for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)
api.update_status('BamPageRo')