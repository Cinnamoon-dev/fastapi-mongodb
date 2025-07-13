#!/usr/bin/env bash

readonly git_path="/home/ubuntu/fastapi-mongodb"

readonly docker_user="cinnamoon"
readonly docker_image="fastapimongopipe"
readonly docker_tag="latest"

echo "PULLING NEW VERSION..."
git -C ${git_path} pull &&
echo "DONE"

echo "STOPPING OLD VERSION..."
docker compose -f compose.deploy.yaml down -t 1 &&
echo "DONE"

echo "PULLING NEW IMAGE..."
docker pull ${docker_user}/${docker_image}:${docker_tag} &&
echo "DONE"

echo "STARTING NEW VERSION..."
docker compose -f compose.deploy.yaml up --build -d &&
echo "DONE"