import tweepy
import threading
from GettingAyah import GettingAyah
from FridaysAndFastingTimes import FridaysAndFastingTimes
import time


API = "JOdcYM9lsJeZWyzvkBVaZ4UF9"
API_secret = "xbEqp0TBM1IbMQ3ief5Z9iRNDqh11A1te0E4FoSMX9jdPybXfE"
token = "1008618754446675968-gdLXz3JHa9Vq6bXgqdoGXhEQ8t9gTE"
token_secret = "mxVfyLUilqHrZDS4cL6lKzylpGuidrphJyGH3bI2ANVGM"

auth = tweepy.OAuthHandler(API, API_secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def TweetAyah():
    while True:
        try:
            api.update_status(GettingAyah())
            time.sleep(60*3)  # 60 second then multiply by the number of minutes you want to pause eg. 10
        except tweepy.TweepError:
            api.update_status(f"({GettingAyah()})")
            time.sleep(60*3)  # 60 second then multiply by the number of minutes you want to pause eg. 10


def TweetFastingTimesAndFridays():
    while True:
        api.update_status(FridaysAndFastingTimes())


thread1 = threading.Thread(target=TweetFastingTimesAndFridays)
thread2 = threading.Thread(target=TweetAyah)
thread1.start()
thread2.start()
