from elasticsearch import Elasticsearch
from bot import Bot
import sys
import os
import docker
import time


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
            volume_driver="local",
            volumes={
                os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "data/es_vol"
                ): {
                    "bind": "/usr/share/elasticsearch/data",
                    "mode": "rw",
                }
            },
        )
        print("elasticsearch launched")
    except docker.errors.APIError:
        print(
            "Could not connect to docker API, Please ensure you have Docker installed properly."
        )

    # Wait for Elastic Search to be ready
    es_client = Elasticsearch(["localhost:9200"])
    print("Opened connection")
    print("Waiting for elastic search nodes to start up...")
    for _ in range(1000):
        try:
            es_client.cluster.health()
            return es_client
        except Exception:
            time.sleep(0.1)
    else:
        print("Timed out, please try again")
        sys.exit()
