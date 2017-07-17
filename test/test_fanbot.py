"""Test module for fanbot"""

from fanbot import fanbot
from fanbot import compliments, secrets

def test_simple():
    """Ensure testing is working"""
    assert 2 + 2 == 4

class TestFanBot:
    """Tests the fanbot class"""

    def setup_class(self):
        self.compliments = compliments.COMPLIMENTS
        self.fanbot = fanbot.Fanbot(
            secrets.TARGET,
            secrets.USERNAME,
            compliments.COMPLIMENTS,
            secrets.CONSUMER_KEY,
            secrets.CONSUMER_SECRET,
            secrets.ACCESS_TOKEN,
            secrets.ACCESS_TOKEN_SECRET
        )

    def test_fanbot_can_compliment(self):
        assert self.fanbot.compliment() in self.compliments

    def test_fanbot_can_connect_to_twitter(self):
        assert self.fanbot.is_connected()

    def test_fanbot_can_be_created_from_modules(self):
        f = fanbot.Fanbot.create_from_modules(secrets, compliments)
        assert f.is_connected()
