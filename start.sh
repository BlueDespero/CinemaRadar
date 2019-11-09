#!/bin/bash
sudo docker run -p 4444:4444 -v /dev/shm:/dev/shm  -it --rm cinema_docker /workspace/run.sh