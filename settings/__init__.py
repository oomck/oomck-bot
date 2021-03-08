import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ES_URL = "localhost:9200"
ES_INDEX_NAME = "fast_and_furious"
ES_TIMEOUT = 30
ES_RETRY_ON_TIMEOUT = True

DATA_URL = os.path.join(BASE_DIR, "data/data.json")

STOP_WORDS_URL = os.path.join(BASE_DIR, "data/stop.txt")
