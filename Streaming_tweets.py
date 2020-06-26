import tweepy

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        self.process_data(raw_data)

        return True

    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


class MaxStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self):
        self.stream.filter(track=['Time'])


#listener = MyStreamListener()
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#stream = MaxStream(auth, listener)
#stream.start()



