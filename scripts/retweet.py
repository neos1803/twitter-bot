from config import init_api
import tweepy
import logging

log = logging.getLogger()

class Retweet(tweepy.StreamListener):
    def __init__(self, api):
        print(api)
        self.api = api
        # Get the authenticated user
        self.me = api.me()
    
    def on_status(self, tweet):
        # log.info(f"Processing the tweet")
        print("Processing the tweet")
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                log.error("Error favoriting", exc_info=True)
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                log.error("Error retweeting", exc_info=True)
    
    def on_error(self, status):
        log.error(status)

def main(words):
    print("Running")
    api = init_api()
    find_tweets = Retweet(api)
    stream = tweepy.Stream(api.auth, find_tweets)
    stream.filter(track=words, languages=["ja"])

if __name__ == "__main__":
    main(["村山 彩希", "ゆいりー"])