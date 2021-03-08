from bot import Bot

bot = Bot()

while True:
    user_input = input("[YOU] ")
    if user_input == "exit":
        break
    print("[BOT] " + bot.ask(user_input))

