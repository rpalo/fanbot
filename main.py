"""Main loop program for the Fan Bot"""

import schedule
import time

from fanbot.fanbot import Fanbot
from fanbot import secrets

# Initially hardcoding a schedule.  Could be swapped out later
bot = Fanbot(secrets.TARGET)
bot.hello_world()
try:
    schedule.every(15).seconds.do(bot.post_compliment())
    # schedule.every().day.at("10:30").do(bot.post_compliment())
except KeyboardInterrupt:
    bot.goodbye()


