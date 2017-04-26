"""Fanbot class that drives the twitter account"""

from .compliments import COMPLIMENTS

import random

class Fanbot:
    def compliment(self):
        return random.choice(COMPLIMENTS)