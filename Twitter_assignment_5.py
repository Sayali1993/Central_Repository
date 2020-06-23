from credentials import *
import tweepy
from pandas import DataFrame

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)


tweets = api.user_timeline(screen_name='user_name',
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts=False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode='extended'
                           )

for info in tweets:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")