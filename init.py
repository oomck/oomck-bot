from elasticsearch import Elasticsearch
from bot import Bot
import sys
import os
import pandas as pd
import glob
import json
from utils.process import filter_data

kaggle_src = "rtatman/ubuntu-dialogue-corpus"

proj_path = os.path.abspath(os.path.dirname(__file__))

# IPMORT DATA

if not os.path.isdir(os.path.join(proj_path, "data/Ubuntu-dialogue-corpus")):
    os.system(
        "kaggle d download " + kaggle_src + " -p " + os.path.join(proj_path, "data")
    )
    os.system(
        "unzip -q "
        + os.path.join(proj_path, "data/ubuntu-dialogue-corpus.zip")
        + " -d "
        + os.path.join(proj_path, "data")
    )
    os.system("rm " + os.path.join(proj_path, "data/ubuntu-dialogue-corpus.zip"))

# PROCESS DATA

if not os.path.isfile(os.path.join(proj_path, "data/data.json")):
    os.chdir(os.path.join(proj_path, "data/Ubuntu-dialogue-corpus"))

    # Get all CSVs
    all_filenames = [i for i in glob.glob("*.{}".format("csv"))]

    # Merge into one CSV
    print("Merging CSVs... (This may take a while)")
    csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    print("Done.")

    # filter data convert to JSON
    # FORMAT: {
    #    prompt: string,
    #    reponse: string
    # }
    json_data = json.dumps(filter_data(csv.iterrows()))

    # Save to file
    f = open(os.path.join(proj_root, "../data.json"), "x")
    f.write(json_data)
    f.close()

# Connect to Elastic search
# esclient = Elasticsearch(["localhost:9200"])

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
