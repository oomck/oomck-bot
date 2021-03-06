from bot import Bot
from es.data_loader import DataLoader

bot = Bot()
data_loader = DataLoader()

print("Welcome to Oomck-Bot! Please type your message below:\nWaiting on you...")
data_loader.load_data()

while True:
    user_input = input("[YOU] ")
    if user_input == "exit":
        break
    if user_input == "load_data":
        data_loader.load_data()
        print("Data has been loaded.")
    else:
        print("[BOT] " + bot.ask(user_input))

