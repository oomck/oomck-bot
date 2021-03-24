import eel
import random
from datetime import datetime


eel.init("web")

@eel.expose
def query_bot(text):
    print(text)
    eel.send_bot_response("test")

@eel.expose
def load_data():
    print("load Data")

eel.start("index.html")
