"""Main loop program for the Fan Bot"""

import logging
import time

import schedule

from fanbot.fanbot import Fanbot
from fanbot import compliments, secrets

logging.basicConfig(level=logging.INFO)

bot = Fanbot(
    secrets.TARGET,
    secrets.USERNAME,
    compliments.COMPLIMENTS,
    secrets.CONSUMER_KEY,
    secrets.CONSUMER_SECRET,
    secrets.ACCESS_TOKEN,
    secrets.ACCESS_TOKEN_SECRET
)

bot.hello_world()
try:
    # Initially hardcoding a schedule.  Could be swapped out later
    # PLACE YOUR CUSTOM SCHEDULES HERE.  SEE SCHEDULE MODULE DOCUMENTATION.
    schedule.every(30).seconds.do(bot.respond_to_tweets)
    schedule.every().day.at("10:30").do(bot.post_compliment)
    while True:
        schedule.run_pending()
        # You can tune the sleep length too.  Should be roughly the same
        # as the most frequently scheduled job above
        time.sleep(30) # seconds

except KeyboardInterrupt:
    bot.goodbye()



