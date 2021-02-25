from elasticsearch import Elasticsearch
from bot import Bot
import sys
import os
import docker


def ensure_elastic():
    # Connect to Docker API
    client = docker.from_env()
    try:
        # Check if container exists
        es = client.containers.get("oomck-elasticsearch")
        # Check if container is running
        if not es.status == "running":
            # Start container
            es.start()
            print("elasticsearch container started")
        else:
            print("elasticsearch already running")
    except docker.errors.NotFound:
        # Create and launch Container
        client.containers.run(
            image="elasticsearch:7.6.2",
            name="oomck-elasticsearch",
            ports={"9200": "9200", "9300": "9300"},
            environment=["discovery.type=single-node"],
            detach=True,
        )
        print("elasticsearch launched")
    except docker.errors.APIError:
        print(
            "Could not connect to docker API, Please ensure you have Docker installed properly."
        )

    # Wait for Elastic Search to be ready
    # client = Elasticsearch(["localhost:9200"])
    # for _ in range(10000):
    #     try:
    #         client.cluster.health(wait_for_status="yellow")
    #         return client
    #     except ConnectionError:
    #         time.sleep(0.1)
    # else:
    #     print("Elastic Search Failed to start")
    #     sys.exit()


ensure_elastic()

client = Elasticsearch(["localhost:9200"])

# EXAMPLE QUERY

response = client.search(
    index="social-*",
    body={
        "query": {"match": {"message": "myProduct"}},
        "aggs": {"top_10_states": {"terms": {"field": "state", "size": 10}}},
    },
)

print(response)


# Prompt example
# b = Bot()
# input = b.prompt_user("TEST")
# print(b.process_input(input))
