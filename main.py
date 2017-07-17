"""Main loop program for the Fan Bot"""

import argparse
import logging
import time

import schedule

from fanbot.fanbot import Fanbot
from fanbot import compliments, secrets

logging.basicConfig(level=logging.INFO)

def main(greeting=True):
        
    bot = Fanbot.create_from_modules(secrets, compliments)
    
    if greeting:
        bot.hello_world()
    try:
        # Initially hardcoding a schedule.  Could be swapped out later
        # PLACE YOUR CUSTOM SCHEDULES HERE.  SEE SCHEDULE MODULE DOCUMENTATION.
        schedule.every(30).minutes.do(bot.respond_to_tweets)
        schedule.every().day.at("10:30").do(bot.post_compliment)
        while True:
            schedule.run_pending()
            # You can tune the sleep length too.  Should be roughly the same
            # as the most frequently scheduled job above
            time.sleep(30*60) # seconds

    except KeyboardInterrupt:
        if greeting:
            bot.goodbye()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tell a FanBot what to do.")
    parser.add_argument("--no-greeting", dest="greet", action='store_false',
                    help="Mutes initial startup message.")
    args = parser.parse_args()
    main(greeting=args.greet)

