import tweepy
import time

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)

for user in tweepy.Cursor(api.followers, screen_name="user_name").items():
    print('follower: ' + user.screen_name)


