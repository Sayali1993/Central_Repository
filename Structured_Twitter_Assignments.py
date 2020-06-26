from twitter import *
from Streaming_tweets import *
from credentials import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_list_of_all_your_tweets():
    tweets = api.user_timeline(screen_name=user_name,
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts=False,
                               tweet_mode='extended'
                               )

    for info in tweets:
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")

def get_list_of_all_your_followers():
    for user in tweepy.Cursor(api.followers, screen_name=user_name, count=200).items():
        print('follower: ' + user.screen_name)

def get_given_num_of_your_tweets_in_given_time():
    tweets = api.user_timeline(screen_name=user_name,
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts=False,
                               tweet_mode='extended'
                               )

    for info in tweets[:numberOfTweets]:
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")

def get_data_from_timeline():
    t = Twitter(
        auth=OAuth(access_token, access_token_secret,
                   consumer_key, consumer_secret))
    x = t.statuses.home_timeline(screen_name=user_name)

    for i in range(0, numberOfTweets):
        print (x[i]['user']['screen_name'])
        print (x[i]['text'])
        print ("_______________________________")

    return x

def get_dynamic_streaming():
    listener = MyStreamListener()
    stream = MaxStream(auth, listener)
    stream.start()



get_list_of_all_your_tweets()
get_list_of_all_your_followers()
get_given_num_of_your_tweets_in_given_time()
get_data_from_timeline()
get_dynamic_streaming()