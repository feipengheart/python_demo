docker stop demo
docker rm demo

docker run -itd --gpus '"device=1"' --name demo --network host \
-v `pwd`:/opt/AI/app \
-w /opt/AI/app \
web_layout:v1.0 /bin/bash
