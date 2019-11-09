#!/bin/bash
sudo docker run -p 4444:4444 -v /dev/shm:/dev/shm  -it cinema_docker /workspace/run.sh