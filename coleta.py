# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import keys
import util 
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=keys.CONSUMER_KEY
consumer_secret=keys.CONSUMER_SECRET

# After the step above, you will be redirected to your app s page.
# Create an access token under the the "Your access token" section
access_token=keys.ACCESS_TOKEN
access_token_secret=keys.ACCESS_TOKEN_SECRET

class StdOutListener(StreamListener):
    """
    A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        #print (data)
        json_data = json.loads(data)
        id = ""
        user = ""
        retweeted_status = False
        originalUser = ""
        text = ""
        if 'id' in json_data:
            id = str(json_data['id'])
        if 'user' in json_data:
            user = ascii(json_data['user']['name'])
        if 'retweeted_status' in json_data:
            retweeted_status = True
            originalUser = ascii(json_data['retweeted_status']['user']['name'])
        if 'text' in json_data:
            text = util.pre_process_tweet(json_data['text'])
        util.persist_at(conn, id, text, user, retweeted_status , originalUser)
       
        return True

    def on_error(self, status):
        print (status)
        if status == 420:
            return True

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    conn = util.conexao()

    stream = Stream(auth, l)
    setTerms = ['#FLAxPAL']
    stream.filter(track=setTerms)
    conn.close()