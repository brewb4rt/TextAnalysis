from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

class textLoader:

    def fromTXT(self, pathToFile):
        return open(pathToFile).readlines()

    def fromTwitter(self, pathToTwitterAccess, ):

        #Variables that contains the user credentials to access Twitter API read from a personal json file
        twitterAccess = json.load(open(pathToTwitterAccess))
        access_token = twitterAccess['Access Token']
        access_token_secret = twitterAccess['Access Token Secret']
        consumer_key = twitterAccess['API Key']
        consumer_secret = twitterAccess['API Secret']

        #This is a basic listener that just prints received tweets to stdout.
        class StdOutListener(StreamListener):
            text=[]

            def on_data(self, data):
                self.text.append(data)
                return True

            def on_error(self, status):
                print status


        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        return l.text