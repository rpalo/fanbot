"""Test module for fanbot"""

from fanbot import fanbot
from fanbot import compliments

def test_simple():
    """Ensure testing is working"""
    assert 2 + 2 == 4

class TestFanBot:
    """Tests the fanbot class"""

    def setup_class(self):
        self.compliments = compliments.COMPLIMENTS

    def setup_method(self):
        self.fanbot = fanbot.Fanbot()

    def test_fanbot_can_compliment(self):
        assert self.fanbot.compliment() in self.compliments

    def test_fanbot_can_connect_to_twitter(self):
        assert self.fanbot.is_connected()



