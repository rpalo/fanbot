# FanBot

A twitter bot to compliment people and make them feel happy.

## Features

 - Randomly tweets a random compliment from compliments.txt at your target
 - Can be asked for an immediate compliment
 - Includes lock.py for autorestarting upon server restart

## Future Features

 - Posse mode?  Retweet with hype!
 - Learns from target's tweets?
 - Target can tell bot how frequently to post?
 - Console mode for debugging?
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
 12. Run the tests to make sure everything's working right.  In the main folder, simply type `pytest`.  (As is evident, this uses Pytest.  If you prefer `nose` or another testing tool, you might have to do some tweedling before you can test.  Or maybe not.  Not sure.)
 13. Let 'er rip!  `python3 main.py`
 13. (Optional) Set up your bot [as a service](#setting-up-as-a-service) so it will run on a remote server and have output logs and you can leave it alone the "right way".

## Setting Up as a Service

Included in the main folder is a file `fanbot.service`.  

1. You'll need to edit this folder to include the **absolute** path to your python executable and your `main.py` file.  You can also include any command-line arguments.  
2. Once you've got your service file ready, copy it to `/lib/systemd/system`:
    ```bash
    sudo cp fanbot.service /lib/systemd/system/fanbot.service
    ```
3. It needs permissions of 644 to work: 
    ```bash
    sudo chmod 644 /lib/sytemd/system/fanbot.service
    ```  
4. Then referesh `systemd` to make sure it's managing your service:
    ```bash
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable fanbot.service
    ```
5. Make sure everything works properly:
    ```bash
    $ sudo reboot
    ...
    $ sudo systemctl status fanbot.service
    # You should see something good like "active" with a few startup logs.
    ```
6. (Optional) To run the service from inside your virtual environment, simply point the python executable to the one in your .venv folder (i.e. /home/{{ you }}/fanbot/.venv/bin/python).  The rest will work as expected.

Once this whole process is complete, you can check the logs on your bot via:

```bash
$ sudo journalctl -e -u fanbot.service
# -e scrolls you to the end of the logs
# -u fanbot.service specifies which service to view.
# You can also use -f or --follow to watch the logs come through live (like `tail`)
```

## Customization

If you've gotten this far, hopefully you are comfortable editing files etc.  All of the randomized compliments are kept in [compliments.py](https://github.com/rpalo/fanbot/blob/master/fanbot/compliments.py).  You can modify the start-up/shut-down messages in [fanbot.py](https://github.com/rpalo/fanbot/blob/master/fanbot/fanbot.py).  Please please please don't check your actual [secrets.py](https://github.com/rpalo/fanbot/blob/master/fanbot/secrets.sample.py) into your repository without encryption.

## Contributions

I've never really had anybody contribute to any of my projects before, but I'm super open to it.  I would almost say it might be a good idea to lay out a rough skeleton of your changes and open the pull request up front so we can talk about it before you do a bunch of work.  

## Code of Conduct

I don't think I'll need this, but it can't hurt.  Obviously the code of conduct comes down to the "Don't Be a Fartknuckle" System™.  To get a good feel for what it means to Not Be a Fartknuckle, check out the [Ubuntu Code of Conduct](https://www.ubuntu.com/about/about-ubuntu/conduct).  If you have any problems, don't hesitate to let me know.  If I give you problems, ditto, but additionally make sure you call me a Fartknuckle.

