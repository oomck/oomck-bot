from elasticsearch import Elasticsearch
from bot import Bot
import sys
import os

kaggle_src = "rtatman/ubuntu-dialogue-corpus"

# Download and unpack
if not os.path.isdir("./data/Ubuntu-dialogue-corpus"):
    os.system("kaggle d download " + kaggle_src + " -p ./data")
    os.system("unzip -q ./data/ubuntu-dialogue-corpus.zip -d ./data")
    os.system("rm ./data/ubuntu-dialogue-corpus.zip")


# Connect to Elastic search
esclient = Elasticsearch(["localhost:9200"])

# EXAMPLE QUERY
#
# response = esclient.search(
#     index='social-*',
#     body={
#         "query": {
#             "match": {
#                 "message": "myProduct"
#             }
#         },
#         "aggs": {
#             "top_10_states": {
#                 "terms": {
#                     "field": "state",
#                     "size": 10
#                 }
#             }
#         }
#     }
# )

# Prompt example
# b = Bot()
# input = b.prompt_user("TEST")
# print(b.process_input(input))
