import sys
import os

sys.path.append(sys.path[0] + "/../")

from bot import Bot
from es.data_loader import DataLoader
import eel
import socket

bot = Bot()
data_loader = DataLoader()

data_loader.load_data()

HOST = "HOST_ADDRESS"
PORT = 4000

# Number of responses
RANGE = 15

# Connect as a client to other host (Group 28)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(RANGE):

        # Receive msg
        msg = s.recv(1024).decode("utf-8")
        print("OTHER CHATBOT: ", msg)

        # Generate response
        response = bot.ask(msg)
        print("OOMCK: ", response + "\n\n")

        # Send response
        s.send(bytes(response, "utf-8"))
