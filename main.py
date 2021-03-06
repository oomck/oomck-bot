import init
from text_parser import Parser
from bot import Bot

client = init.ensure_elastic()
parser = Parser()
bot = Bot(parser, client)

while True:
    user_input = bot.get_input()
    if user_input == "kill program":
        break
    bot.get_answer(user_input)
