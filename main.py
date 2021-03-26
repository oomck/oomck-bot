from bot import Bot
import nltk
from es.data_loader import DataLoader
import eel

nltk.download("punkt")

bot = Bot()
data_loader = DataLoader()

data_loader.load_data()

eel.init("web")


@eel.expose
def query_bot(user_input):
    eel.send_bot_response(bot.ask(user_input))


eel.start("index.html")
