# twitter-bot/scripts/config.py

from decouple import config
import tweepy
import logging

log = logging.getLogger()

def init_api():
    auth = tweepy.OAuthHandler(config('API_KEY'), config('API_SECRET_KEY'))
    auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        log.error('Error while creating API', exc_info=True)
        raise e
    log.info('API initialized')
    print('API initialized')
    return api