import init
from text_parser import Parser
from bot import Bot

client = init.ensure_elastic()
bot = Bot(client)
print(bot.get_input())
bot.get_answer("open documents")
