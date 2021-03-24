import unittest

from bot import Bot


class TestBot(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBot, self).__init__(*args, **kwargs)
        self.bot = Bot()

    def test_bot(self):
        self.assertEqual(self.bot.ask("hi"), "Hey.")
        self.assertEqual(self.bot.ask("sadfkljdfkjlhfd"), "Sorry, I don't get what you're saying, can you try again?")
