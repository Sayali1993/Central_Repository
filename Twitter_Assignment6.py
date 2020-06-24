import datetime
import tweepy

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)
username = 'TimesNow'
startDate = datetime.datetime(2020, 6, 24, 2, 0, 0)
endDate = datetime.datetime(2020, 6, 24, 2, 30, 0)
tweets = []
tmpTweets = api.user_timeline(username)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

print("\nTweets of: {} ".format(username).upper())
print("\n")


count = 0
for user in tweets[:3]:
    count = count + 1
    print("Tweet {} ".format(count))
    print("ID: {}".format(user.id))
    print("Date Time: {}".format(user.created_at))
    print(user.text)
    print("\n")



