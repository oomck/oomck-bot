from elasticsearch import Elasticsearch
from bot import Bot

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
b.prompt_user("TEST")
