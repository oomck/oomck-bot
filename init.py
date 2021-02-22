from elasticsearch import Elasticsearch
from bot import Bot
import sys
import os

# Download data
data_repo = "https://github.com/google-research-datasets/ccpe"

if not os.path.isdir("./ccpe"):
    os.system("git clone " + data_repo)


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
b = Bot()
input = b.prompt_user("TEST")
print(b.process_input(input))
