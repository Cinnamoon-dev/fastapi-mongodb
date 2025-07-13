#!/bin/bash

readonly git_path="/home/ubuntu/fastapi-mongodb"

readonly docker_user="cinnamoon"
readonly docker_image="fastapimongopipe"
readonly docker_tag="latest"

echo "PULLING NEW VERSION..."
git -C ${git_path} pull &&
echo "DONE"

echo "STOPPING OLD VERSION..."
sudo docker compose -f ${git_path}/compose.prod.yaml down -t 1 &&
echo "DONE"

echo "PULLING NEW IMAGE..."
sudo docker pull ${docker_user}/${docker_image}:${docker_tag} &&
echo "DONE"

echo "STARTING NEW VERSION..."
sudo docker compose -f ${git_path}/compose.prod.yaml up --build -d &&
echo "DONE"