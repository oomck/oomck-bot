from elasticsearch import Elasticsearch
import sys
import os
import shutil
import docker
import time
import gdown
from zipfile import ZipFile


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
            # volume_driver="local",
            # volumes={
            #     os.path.join(
            #         os.path.dirname(os.path.abspath(__file__)), "data/es_vol"
            #     ): {
            #         "bind": "/usr/share/elasticsearch/data",
            #         "mode": "rw",
            #     }
            # },
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
    for _ in range(10000):
        try:
            es_client.cluster.health(wait_for_status="yellow")
            return es_client
        except Exception:
            time.sleep(0.1)
    else:
        print("Timed out, please try again")
        sys.exit()

# def setup_data():
#     url = "https://drive.google.com/uc?id=1cypZd534vcbn4OL9vMNYwpssSLF9_IZC"
#     basepath = os.path.dirname(os.path.abspath(__file__))
#     download_output = os.path.join(basepath, "data/es_vol.zip")
#     zip_output = os.path.join(basepath, "data")
#
#     # Download Zip from GDrive if it doesn't already exist
#     if not os.path.exists(download_output):
#         gdown.download(url, download_output, quiet=False)
#
#     # Unzip download to data/es_vol
#     # (Run on new container creation even if the folder already exists)
#     print("Unzipping...")
#     # Remove folder if already exists
#     if os.path.isdir(os.path.join(zip_output, "es_vol")):
#         shutil.rmtree(os.path.join(zip_output, "es_vol"))
#     # Extract
#     with ZipFile(download_output, "r") as zip:
#         zip.extractall(zip_output)
