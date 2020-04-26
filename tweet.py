from twython import Twython
from twython import TwythonError
import os
tweetmode = False
def writeTweet(tweet):
        if tweetmode:
            from auth import (
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )
            twitter = Twython(
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )
            try:
                twitter.update_status(status=tweet)
            except TwythonError as e:
                print("Error with tweet")
                print(e)
                os.system("pause")

