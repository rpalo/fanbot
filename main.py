"""Main loop program for the Fan Bot"""

import argparse
import logging
import socket
import time

import schedule

from fanbot.fanbot import Fanbot
from fanbot import compliments, secrets

logging.basicConfig(level=logging.INFO)

def main(greeting=True):
        
    bot = Fanbot(
        secrets.TARGET,
        secrets.USERNAME,
        compliments.COMPLIMENTS,
        secrets.CONSUMER_KEY,
        secrets.CONSUMER_SECRET,
        secrets.ACCESS_TOKEN,
        secrets.ACCESS_TOKEN_SECRET
    )
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

def check_and_aquire_lock():
    """Aquires a lock socket so the auto-restart service knows we're
    running"""
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_id = "rpalo.fanbot"
        sock.bind("\0" + lock_id)
        logging.info("Aquired lock at %r", lock_id)
        return True
    except socket.error:
        logging.warning("Couldn't re-lock %r.  Bot could be already running?", lock_id)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tell a FanBot what to do.")
    parser.add_argument("--no-greeting", dest="greet", action='store_false',
                    help="Mutes initial startup message.")
    parser.add_argument("--lock", dest="lock", action="store_true",
                    help="Locks a socket to allow for automatic restarting")
    args = parser.parse_args()
    if args.lock:
        check_and_aquire_lock()
    main(greeting=args.greet)

