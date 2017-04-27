"""Contains Fanbot class that drives the twitter account"""

import random
import tweepy

from .compliments import COMPLIMENTS
from . import secrets

class Fanbot:
    """Drives fanbot twitter account"""
    def __init__(self, idol_user):
        self.connect()
        # Be sure to include @ in front of username
        self.idol = idol_user

    def compliment(self):
        """Returns a random compliment"""
        return random.choice(COMPLIMENTS)

    def is_connected(self):
        """Returns true if bot can connect to twitter"""
        return self.api.verify_credentials()

    def connect(self):
        """Connects bot to twitter and handles authentication"""
        auth = tweepy.OAuthHandler(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)
        auth.set_access_token(secrets.ACCESS_TOKEN, secrets.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def post_compliment(self):
        """Posts a compliment at its target"""
        compliment = self.compliment()
        tweet = "{} {}".format(self.idol, compliment)
        return self.api.update_status(tweet)

    def print_compliment(self):
        """Print a compliment at its target"""
        compliment = self.compliment()
        tweet = "{} {}".format(self.idol, compliment)
        print(tweet)

    def hello_world(self):
        """Posts a status stating the bot is now in control."""
        tweet_options = [
            "Fan Bot is online.",
            "FanBot logged in and ready to adore!",
            "Hello, world!  Fan Bot is up and running!"
        ]
        tweet = random.choice(tweet_options)
        return self.api.update_status(tweet)

    def goodbye(self):
        tweet_options = [
            "Signing off for now!",
            "Fan Bot shutting down.",
            "Logging off.  Bye Felicia!",
        ]
        tweet = random.choice(tweet_options)
        return self.api.update_status(tweet)



    