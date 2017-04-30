"""Contains Fanbot class that drives the twitter account"""

import random
import tweepy

class Fanbot:
    """Drives fanbot twitter account"""
    def __init__(self, target_username, compliment_list,
                consumer_key, consumer_secret, access_token, access_token_secret):
        self.compliments = compliment_list
        # Secrets not stored within instance for security reasons.
        # Also, not looked up from .secrets directly because that could
        # be a messy API.  Cleaner to have the user specify where the
        # secrets, target, and compliments come from.
        self.connect(consumer_key, consumer_secret, access_token, access_token_secret)
        # Be sure to include @ in front of username
        self.target = target_username

    def compliment(self):
        """Returns a random compliment"""
        return random.choice(self.compliments)

    def is_connected(self):
        """Returns true if bot can connect to twitter"""
        return self.api.verify_credentials()

    def connect(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """Connects bot to twitter and handles authentication"""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
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



    