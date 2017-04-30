"""Main loop program for the Fan Bot"""

import time

import schedule

from fanbot.fanbot import Fanbot
from fanbot import compliments, secrets

# Initially hardcoding a schedule.  Could be swapped out later
bot = Fanbot(
    secrets.TARGET,
    compliments.COMPLIMENTS,
    secrets.CONSUMER_KEY,
    secrets.CONSUMER_SECRET,
    secrets.ACCESS_TOKEN,
    secrets.ACCESS_TOKEN_SECRET
)

bot.hello_world()
try:

    # PLACE YOUR CUSTOM SCHEDULES HERE.  SEE SCHEDULE MODULE DOCUMENTATION.
    # schedule.every(15).seconds.do(bot.post_compliment)
    schedule.every().day.at("10:30").do(bot.post_compliment)
    while True:
        schedule.run_pending()
        # You can tune the sleep length too.  Since I'm only having it
        # run one compliment per day, I have an hourly check in.
        time.sleep(3600)

except KeyboardInterrupt:
    bot.goodbye()



