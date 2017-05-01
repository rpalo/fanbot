# FanBot

A twitter bot to compliment people and make them feel happy.

## Features

 - Randomly tweets a random compliment from compliments.txt at your target
 - Can be asked for an immediate compliment

## Future Features

 - Posse mode?  Retweet with hype!
 - Learns from target's tweets?
 - Target can tell bot how frequently to post?
 - Console mode for debugging?
 - Main.py --no-greeting argument
 - Command line arg for printing tweets instead of tweeting to API for debugging.
 - Quick install tool?  I'm not sure if the install process is too long or not.

## Installation and Operation

Installation should go pretty quickly.

 1. Clone this repository - `git clone https://github.com/rpalo/fanbot.git && cd fanbot`
 2. (Optional) Create a virtual environment for the application - `python3 -m venv .venv`  If you name it `.venv`, the .gitignore file will ignore it by default.
 3. (Required only if you did step 2) Activate your virtual environment
  - Windows PowerShell: `.venv/scripts/activate`
  - *nix: `source .venv/bin/activate`
 4. Install the required packages - `pip3 install -r requirements.txt`
 5. Create your secrets file - `mv fanbot/secrets.sample.py fanbot/secrets.py`
 6. Create a twitter account for your bot.
 7. *While logged in as this bot,* create a [twitter app](https://apps.twitter.com) for your bot.
 8. From the "Keys and Access Tokens" tab of your new app, create a new key.
 9. Take note of your Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
 10. Fill these values into your `secrets.py` file.  Also fill in the username of the account you wish to be a fan of.
 11. Fill out the `main.py` file with instructions of your own.  Take note of Twitter's [rate limiting policy.](https://dev.twitter.com/rest/public/rate-limiting)  See the [schedule module documentation](https://pypi.python.org/pypi/schedule) for more info.
 12. Let 'er rip!  `python3 main.py`

Currently, I'm working on setting up logging and other things, so you'll have to figure out how you want to keep your script running.  If you have ideas let me know.  I've got a [PythonAnywhere](https://pythonanywhere.com) instance that I just spun up and keep running in terminal mode.

## Customization

If you've gotten this far, hopefully you are comfortable editing files etc.  All of the randomized compliments are kept in [compliments.py](https://github.com/rpalo/fanbot/blob/master/fanbot/compliments.py).  You can modify the start-up/shut-down messages in [fanbot.py](https://github.com/rpalo/fanbot/blob/master/fanbot/fanbot.py).  Please please please don't check your actual [secrets.py](https://github.com/rpalo/fanbot/blob/master/fanbot/secrets.sample.py) into your repository without encryption.

## Contributions

I've never really had anybody contribute to any of my projects before, but I'm super open to it.  I would almost say it might be a good idea to lay out a rough skeleton of your changes and open the pull request up front so we can talk about it before you do a bunch of work.  

## Code of Conduct

I don't think I'll need this, but it can't hurt.  Obviously the code of conduct comes down to the "Don't Be a Fartknuckle" System™.  To get a good feel for what it means to Not Be a Fartknuckle, check out the [Ubuntu Code of Conduct](https://www.ubuntu.com/about/about-ubuntu/conduct).  If you have any problems, don't hesitate to let me know.  If I give you problems, ditto, but additionally make sure you call me a Fartknuckle.

