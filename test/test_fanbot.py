from fanbot import fanbot
from fanbot import compliments

def test_simple():
    assert 2 + 2 == 4

class TestFanBot:
    def setup_class(self):
        self.compliments = compliments.COMPLIMENTS

    def setup_method(self):
        self.fanbot = fanbot.Fanbot()
    
    def test_fanbot_can_compliment(self):
        assert self.fanbot.compliment() in self.compliments
