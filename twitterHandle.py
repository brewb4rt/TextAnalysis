#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
#Variables that contains the user credentials to access Twitter API read from a personal json file
twitterAccess = json.load(open("D:\\Proggin\\Python\\TextAnalysis\\twitterZugang.json"))
access_token = twitterAccess['Access Token']
access_token_secret = twitterAccess['Access Token Secret']
consumer_key = twitterAccess['API Key']
consumer_secret = twitterAccess['API Secret']


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])