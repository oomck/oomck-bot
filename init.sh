#!/usr/bin/env bash
set -euo pipefail

if [ ! "$(docker ps -q -f name=oomck-elasticsearch)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=oomck-elasticsearch)" ]; then
        # cleanup
        docker rm oomck-elasticsearch
    fi
    # run your container
    docker run -d --name oomck-elasticsearch -p 9300:9300 -p 9200:9200 elasticsearch:7.6.2
fi
