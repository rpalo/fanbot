"""Contains Fanbot class that drives the twitter account"""

from datetime import datetime
import logging
import random
import tweepy

class Fanbot:
    """Drives fanbot twitter account"""
    def __init__(self, target_username, bot_username, compliment_list,
                 consumer_key, consumer_secret, access_token, access_token_secret):
        self.compliments = compliment_list
        # Secrets not stored within instance for security reasons.
        # Also, not looked up from .secrets directly because that could
        # be a messy API.  Cleaner to have the user specify where the
        # secrets, target, and compliments come from.
        self.connect(consumer_key, consumer_secret, access_token, access_token_secret)
        # Be sure to include @ in front of usernames
        self.target = target_username
        self.username = bot_username
        self.most_recent_mention_id = self.most_recent_post().id
        logging.info("Bot created")

    def compliment(self):
        """Returns a random compliment"""
        return random.choice(self.compliments)

    def is_connected(self):
        """Returns true if bot can connect to twitter"""
        return self.api.verify_credentials()

    def most_recent_post(self):
        """Returns the bot's most recent post"""
        bot_user_info = self.api.me()
        return bot_user_info.status

    def connect(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """Connects bot to twitter and handles authentication"""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_compliment(self, extra_text=None):
        """Posts a compliment at its target"""
        compliment = self.compliment()
        tweet = "{} {}".format(self.target, compliment)
        if extra_text:
            tweet += " - " + extra_text
        tweet = tweet[:140] # Stay below char limit
        result = self.api.update_status(tweet)
        logging.info("Posted: %s", result.text)
        return result

    def print_compliment(self, extra_text=None):
        """Print a compliment at its target"""
        compliment = self.compliment()
        tweet = "{} {}".format(self.target, compliment)
        if extra_text:
            tweet += " - " + extra_text
        tweet = tweet[:140]
        print(tweet)

    def hello_world(self):
        """Posts a status stating the bot is now in control."""
        tweet_options = [
            "Fan Bot is online.",
            "FanBot logged in and ready to adore!",
            "Hello, world!  Fan Bot is up and running!"
        ]
        tweet = random.choice(tweet_options)
        # Avoid duplicate status errors
        pretty_time_stamp = datetime.now().strftime("%m-%d %I:%M%p")
        tweet = pretty_time_stamp + " - " + tweet
        logging.info("Sending Hello World Tweet: %s", tweet)
        return self.api.update_status(tweet)

    def goodbye(self):
        """Tweets a sign off message"""
        tweet_options = [
            "Signing off for now!",
            "Fan Bot shutting down.",
            "Logging off.  Bye Felicia!",
        ]
        tweet = random.choice(tweet_options)
        # Avoid Duplicate Status Errors
        pretty_time_stamp = datetime.now().strftime("%m-%d %I:%M%p")
        tweet = pretty_time_stamp + " - " + tweet
        logging.info("Sending Goodbye Tweet: %s", tweet)
        return self.api.update_status(tweet)

    def get_messages(self, filter_target=True):
        """Retrieves a list of messages directed @ fanbot"""
        # Include the "from: " clause to filter by only the target
        if filter_target:
            query = "from:{} {}".format(self.target, self.username)
        else:
            query = self.username
        mentions = self.api.search(query, since_id=self.most_recent_mention_id)
        if mentions:
            results = [{"text": mention.text,
                        "author": mention.author} for mention in mentions]
            self.most_recent_mention_id = mentions[0].id
        else:
            results = []
        return results

    def respond_to_tweets(self):
        """Checks for messages and responds appropriately"""
        # Set flag filter_target=False to allow anybody to prompt bot
        # to respond.  Default is True
        new_messages = self.get_messages(filter_target=False)
        logging.info("Checking messages: %s results", len(new_messages))
        # Simplest implementation tweets a compliment regardless of message
        if new_messages:
            other_requestors = [message["author"].name for message in new_messages
                                if message["author"].screen_name != "Tpaylo"]
            requestor_text = "from {}".format(", ".join(other_requestors))
            self.post_compliment(extra_text=requestor_text)



    