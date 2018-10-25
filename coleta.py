# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

import keys
from util import stopwords_files_to_list
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=keys.CONSUMER_KEY
consumer_secret=keys.CONSUMER_SECRET

# After the step above, you will be redirected to your app s page.
# Create an access token under the the "Your access token" section
access_token=keys.ACCESS_TOKEN
access_token_secret=keys.ACCESS_TOKEN_SECRET

# create a list of stopwords in English, Spanish and Portuguese.
stop_words = stopwords_files_to_list()
class StdOutListener(StreamListener):
   """ A listener handles tweets are the received from the stream.
   This is a basic listener that just prints received tweets to stdout.

   """
   def on_data(self, data):
       #print (data)
       json_data = json.loads(data)
       text = ""
       palavra = ""
       if 'user' in json_data:
           text = ascii(json_data['text'])
           for elem in text.split():
              if palavra not in stop_words:
                 palavra = elem
       if (palavra != ""):
           print("\"" + palavra + "\"" + "\n")
           file.write("\"" + palavra + "\"" + "\n")

       # user = "---"
       # originalUser = "---"
       # if 'user' in json_data:
       #     user = ascii(json_data['user']['name'])
       # if 'retweeted_status' in json_data:
       #     originalUser = ascii(json_data['retweeted_status']['user']['name'])
       # if (user != "---"):
       #     print("\"" + user + "\" \"" + originalUser +"\"" + "\n")
       #     file.write("\"" + user + "\" \"" + originalUser +"\"" + "\n")
       return True

   def on_error(self, status):
       print (status)
       # if status_code == 420:
       #     return True

if __name__ == '__main__':
   file = open('teste.txt', 'a')
   l = StdOutListener()
   auth = OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_token, access_token_secret)

   stream = Stream(auth, l)
   setTerms = ['Boca', 'Benedetto', '#CagueiproIbope ']
   stream.filter(track=setTerms)
