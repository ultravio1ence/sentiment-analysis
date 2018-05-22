from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging
import json
import sys
from pprint import pprint

_log = logging.getLogger(__name__)


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# authorization

access_token = "908156594306916352-EIwQB5f9irymyQ3XHBToDgMGYXaSRnC"
access_token_secret = "mTzAJk6BSmOBNKDnnklSB0s8KAZ7qCABoU2L3FnH5b0GD"
consumer_key = "whV9YdTcAe2U0Wa1XbkLIJexK"
consumer_secret = "iF1AliM3whSyz4d8rFYlsNNI2DwmOKqFEEQXJcElGOSZY3MzOl"

class TwitterListener(StreamListener):
 def __init__(self, phrases):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.__stream = Stream(auth, listener=self, languages=['en'])
    self.__stream.filter(track=['opinion'], async=True)

 def on_connect(self):
        # connection
    print("//YOU ARE NOW CONNECTED TO THE STREAMING API//")
 def disconnect(self):
    self.__stream.disconnect()

 def on_data(self, data):
     print(data)  
     f = open('A:...txt', "w") #file for collecting
     f.write(data)
     f.close
        
 def on_error(self, status):
    print(status)

if __name__ == '__main__':
    import time
    logging.basicConfig(level=logging.INFO)

phrases = open('A:/codes/....txt', encoding='UTF-8', errors='ignore') #file with filters
listener = TwitterListener(phrases)

def on_status(self, status):
        print(status)

def printStatus(self):
    print('English Tweets : {0}'.format(self.count))
    print('Non-English Tweets : {0}'.format(self.nonEngCount))
def on_status(self, status):
    print(status)

def printStatus(self):
    print('English Tweets : {0}'.format(self.count))
    print('Non-English Tweets : {0}'.format(self.nonEngCount))
# time limit and disconnect
time.sleep(480)
listener.disconnect()



